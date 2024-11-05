# backend/app/main.py

from fastapi import FastAPI
from Backend.routers import tasks, users
from Backend.database.models import Base, engine

# Crear todas las tablas de la base de datos al iniciar la aplicación
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir los routers
app.include_router(tasks.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Hola Mundo desde la aplicación principal"}
