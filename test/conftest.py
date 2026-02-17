import pytest
import asyncio
from httpx import AsyncClient
from app.main import app
from app.db.session import get_db

# This allows us to use 'async def test_...'
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

# A mock client that talks to our FastAPI app
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
