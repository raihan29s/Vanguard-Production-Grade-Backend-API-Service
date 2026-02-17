from locust import HttpUser, task, between

class VanguardUser(HttpUser):
    # Simulate a user waiting 1-2 seconds between actions
    wait_time = between(1, 2)
    token = None

    def on_start(self):
        """
        Executed when a simulated user starts. 
        We login once to get a JWT for subsequent requests.
        """
        response = self.client.post("/auth/login", data={
            "username": "test@example.com",
            "password": "securepassword123"
        })
        if response.status_code == 200:
            self.token = response.json().get("access_token")

    @task(3)
    def get_product_cached(self):
        """
        Hits the product endpoint. 
        The '3' weight means this task happens 3x more often than others.
        """
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        # We hit the same ID to trigger the Redis cache
        self.client.get("/products/1", headers=headers, name="/products/[id]")

    @task(1)
    def check_health(self):
        """Simulates a load balancer health check."""
        self.client.get("/health")
