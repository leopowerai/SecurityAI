# backend/tests/test_tasks.py

from fastapi.testclient import TestClient
from Backend.app.main import app

client = TestClient(app)

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola desde la ruta de tareas"}