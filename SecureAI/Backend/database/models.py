# backend/database/models.py

import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

##
# Construir la ruta absoluta para `test.db` en la carpeta `database`
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#DATABASE_PATH = os.path.join(BASE_DIR, 'test.db')
#SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
##

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de conexión a la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Configura la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define la base para los modelos
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)