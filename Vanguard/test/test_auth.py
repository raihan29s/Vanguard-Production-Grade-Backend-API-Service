import pytest

@pytest.mark.asyncio
async def test_register_and_login(client):
    # 1. Test Registration
    user_data = {
        "email": "tester@example.com",
        "password": "testpassword123",
        "full_name": "Test User"
    }
    reg_response = await client.post("/auth/register", json=user_data)
    assert reg_response.status_code == 201
    assert reg_response.json()["email"] == user_data["email"]

    # 2. Test Login
    login_data = {
        "username": "tester@example.com",
        "password": "testpassword123"
    }
    # OAuth2 uses form data, not JSON
    login_response = await client.post("/auth/login", data=login_data)
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    
    # 3. Test Accessing Protected Route
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    me_response = await client.get("/users/me", headers=headers)
    assert me_response.status_code == 200
    assert me_response.json()["email"] == user_data["email"]
