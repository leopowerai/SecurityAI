# backend/tests/test_users.py

from fastapi.testclient import TestClient
from Backend.app.main import app
from Backend.database import schemas

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert "id" in response.json()