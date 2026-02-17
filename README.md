# Vanguard: Enterprise-Grade Retail Backend API

**Vanguard** is a production-ready RESTful service designed for high-concurrency inventory management. It demonstrates modern backend patterns, including asynchronous database operations, multi-layer security, and performance optimization through distributed caching.

---

##  System Architecture

Vanguard utilizes a **Cache-Aside Architecture** to balance data integrity with high performance.

* **API Layer:** FastAPI with `async/await` for non-blocking I/O.
* **Auth Layer:** JWT-based authentication with OAuth2 password flow.
* **Cache Layer:** Redis for sub-millisecond retrieval of frequently accessed resources.
* **Data Layer:** PostgreSQL with SQLAlchemy 2.0 (Async) and Alembic migrations.
* **Ops:** Fully containerized with Docker and ready for AWS deployment.

---

##  Key Performance Metrics

* **Database Latency:** ~80-120ms average response.
* **Cache Latency:** ~5-12ms average response.
* **Throughput:** Scalable to 1,000+ concurrent users (validated via Locust load testing).

---

##  Project Structure

```text
app/
├── api/          # Route handlers & Dependencies
├── core/         # Config (Pydantic), Security, & Redis init
├── db/           # Session management & Database Base
├── models/       # SQLAlchemy ORM Entities
└── schemas/      # Pydantic data validation rules
