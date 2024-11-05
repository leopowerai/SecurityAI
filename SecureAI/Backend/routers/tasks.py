# backend/routers/tasks.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks/")
def read_tasks():
    return {"message": "Hola desde la ruta de tareas"}