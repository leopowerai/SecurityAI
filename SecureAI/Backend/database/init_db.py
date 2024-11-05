# Backend/database/init_db.py

from models import Base, engine

def init_db():
    # Crea todas las tablas definidas en los modelos si no existen
    Base.metadata.create_all(bind=engine)
    print("Base de datos creada exitosamente")

# Ejecuta la función para crear la base de datos cuando se ejecuta el archivo
if __name__ == "__main__":
    init_db()
