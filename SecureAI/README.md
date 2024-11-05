# Proyecto FastAPI con React y Base de Datos

Este proyecto combina un backend en **FastAPI** con una base de datos SQLite (`test.db`) y un frontend en **React**. A continuación se encuentran todas las instrucciones para configurar el entorno de desarrollo, crear la base de datos y ejecutar el proyecto.

---

## Requisitos Previos

- **Python** 3.7 o superior
- **Node.js** y **npm** (para el frontend en React)
- **Git** (para gestionar el repositorio)

---

## Configuración del Entorno de Backend

### 1. Hacer un Fork del Repositorio

Haz un fork del repositorio a tu cuenta de GitHub. Luego, en tu máquina local, clona el repositorio desde tu cuenta:

```bash
git clone <URL_DEL_FORK>
cd <NOMBRE_DEL_PROYECTO>


2. Crear el Entorno Virtual
Para evitar conflictos con otras instalaciones de Python, crea un entorno virtual:

python -m venv venv

3. Activar el Entorno Virtual
Activa el entorno virtual para instalar dependencias en un entorno aislado:

En Unix/macOS:
source venv/bin/activate

En Windows:
.\venv\Scripts\activate

4. Instalar Dependencias
Con el entorno virtual activado, instala las dependencias de Python desde el archivo requirements.txt:
pip install -r requirements.txt

Si no tienes un requirements.txt, puedes crearlo con:
pip freeze > requirements.txt

5. Crear el Archivo .env
Para gestionar la configuración sensible, crea un archivo .env en la raíz del proyecto y añade la URL de la base de datos:
DATABASE_URL=sqlite:///./Backend/database/test.db

6. Crear la Base de Datos
Ejecuta el script de inicialización para crear la base de datos test.db y sus tablas:
python -m Backend.database.init_db

Configuración del Frontend
1. Instalar Dependencias del Frontend
Ve al directorio del frontend y ejecuta el comando de instalación de dependencias de Node.js:

cd frontend
npm install

2. Ejecutar el Servidor de Desarrollo de React
Para iniciar el servidor de desarrollo de React, usa el siguiente comando:

npm start

El frontend estará disponible en http://localhost:3000.

Ejecutar el Proyecto Completo
Con el entorno de backend y frontend configurado, sigue estos pasos para iniciar el proyecto:

1. Inicia el Servidor de FastAPI
Desde la raíz del proyecto (asegúrate de que el entorno virtual esté activado), ejecuta el siguiente comando para iniciar el backend con Uvicorn:

uvicorn Backend.app.main:app --reload

Esto debería iniciar el backend en http://127.0.0.1:8000.

2. Acceder a la Documentación de la API
FastAPI proporciona una documentación interactiva que puedes ver en:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc


3. Iniciar el Frontend
En una terminal separada, asegúrate de estar en el directorio frontend y luego ejecuta:

npm start

El frontend debería abrirse en http://localhost:3000 y estar listo para interactuar con el backend.

Pruebas
Pruebas Automáticas del Backend
Si has configurado pruebas en la carpeta Backend/tests, puedes ejecutarlas usando pytest:

pytest Backend/tests

Esto ejecutará todas las pruebas y mostrará los resultados en la terminal.

Notas Adicionales
.gitignore: Asegúrate de tener un archivo .gitignore configurado para ignorar archivos sensibles como el entorno virtual (venv/), archivos de configuración (.env), dependencias de Node.js (node_modules/) y archivos de la base de datos (test.db).

Desactivación del Entorno Virtual: Cuando termines de trabajar en el proyecto, puedes desactivar el entorno virtual con:

deactivate

Estructura del Proyecto
La estructura básica de tu proyecto debería verse así:

ProjectRoot/
├── Backend/
│   ├── app/
│   │   └── main.py
│   ├── database/
│   │   ├── init_db.py
│   │   └── models.py
│   ├── routers/
│   └── tests/
├── frontend/
│   ├── node_modules/
│   ├── public/
│   └── src/
├── .env
├── .gitignore
├── README.md
└── requirements.txt


¡Con esto deberías tener todo lo necesario para configurar, ejecutar y probar tu proyecto! Si tienes alguna duda o encuentras un problema, revisa la documentación o consulta al equipo de desarrollo.


Este archivo `README.md` proporciona una guía completa sobre la configuración del entorno de backend y frontend, la creación de la base de datos, y el uso del entorno virtual, así como los pasos para iniciar y probar la aplicación.
