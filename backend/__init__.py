import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

# Ensure tables exist in the CI test database
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_shorten_and_redirect_flow():
    # 1. Test creating a short URL
    target_url = "https://github.com/Ashwani0044"
    response = client.post("/api/shorten", json={"long_url": target_url})
    assert response.status_code == 200

    data = response.json()
    assert "short_code" in data
    assert data["long_url"].rstrip("/") == target_url
    assert data["clicks"] == 0

    short_code = data["short_code"]

    # 2. Test redirection (disable follow_redirects to inspect the 307/302 header)
    redirect_res = client.get(f"/{short_code}", follow_redirects=False)
    assert redirect_res.status_code in (302, 307)
    assert redirect_res.headers["location"].rstrip("/") == target_url

    # 3. Test that click count incremented
    stats_res = client.get(f"/api/urls/{short_code}")
    assert stats_res.status_code == 200
    assert stats_res.json()["clicks"] == 1


def test_invalid_short_code_returns_404():
    response = client.get("/nonexistent999", follow_redirects=False)
    assert response.status_code == 404