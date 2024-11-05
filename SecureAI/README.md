<h1 align="center"></>🔐 SecureAI </h1> 
<p align="center">Plataforma de Detección de Anomalías para PyMEs en Colombia</></p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-yellow.svg" />
  <img src="https://img.shields.io/badge/FastAPI-Framework-green.svg" />
  <img src="https://img.shields.io/badge/AI-Integrated-red.svg" />
</p>

## 📌 Descripción

**SecureAI** es una plataforma que combina **inteligencia artificial** y **ciberseguridad** para proteger a las pequeñas y medianas empresas (PyMEs) contra amenazas digitales. Con **SecureAI**, las PyMEs pueden detectar anomalías en sus sistemas, detectar intrusiones y fortalecer su seguridad digital utilizando tecnología avanzada de aprendizaje automático y autenticación segura.

Este proyecto busca capacitar al estudiantes en ciberseguridad e inteligencia artificial, a través del desarrollo de una plataforma para detectar anomalías en sistemas de PyMEs. Los estudiantes aprenderán a implementar un BackEnd en Python usando FastAPI, con un frontend en React. Comenzarán con SQLite como base de datos y migrarán a PostgreSQL en etapas avanzadas. Además, integrarán herramientas de IA como scikit-learn, TensorFlow y PyTorch para la detección de anomalías. La seguridad se implementará con autenticación JWT, hashing de contraseñas con bcrypt y autenticación multifactor. Las infraestructuras de despliegue qus se usarán son Docker, GitHub Actions para CI/CD, AWS y Nginx.

## 🛠️ Características Principales

Permite a las pequeñas empresas en Colombia mejorar su ciberseguridad, protegiéndose de ciberataques con una herramienta accesible. Está especialmente diseñado para empresas con recursos limitados, brindándoles un sistema que detecta patrones anómalos y comportamientos sospechosos, ayudándolas a prevenir potenciales amenazas.

## 📂 Estructura del Proyecto

<p>Este es un desglose de la estructura del proyecto <strong>SecureAI</strong>, incluyendo carpetas y archivos esenciales para el backend y frontend.</p>

<pre>
SecureAI/
├── Backend/
│   ├── app/
│   │   └── main.py               # Punto de entrada principal de la aplicación FastAPI
│   ├── database/
│   │   ├── models.py             # Definición de modelos de base de datos
│   │   └── init_db.py            # Script de inicialización de la base de datos
│   ├── routers/
│   │   ├── tasks.py              # Endpoints de gestión de tareas
│   │   └── users.py              # Endpoints de gestión de usuarios
│   └── tests/
│       ├── test_tasks.py         # Pruebas para los endpoints de tareas
│       └── test_users.py         # Pruebas para los endpoints de usuarios
├── Frontend/
│   ├── node_modules/             # Módulos de Node.js (generado automáticamente)
│   ├── public/
│   │   └── index.html            # Archivo HTML principal del frontend
│   ├── src/
│   │   ├── components/           # Componentes de React
│   │   │   ├── TaskList.js       # Componente para listar tareas
│   │   │   ├── TaskDetail.js     # Componente para detalles de tareas
│   │   │   └── AddTaskForm.js    # Componente para agregar una tarea
│   │   ├── App.jsx               # Componente principal de la aplicación React
│   │   └── index.js              # Punto de entrada del frontend de React
│   ├── .gitignore                # Ignora archivos innecesarios en el frontend
│   ├── eslint.config.js          # Configuración de ESLint para el frontend
│   ├── package-lock.json         # Archivo de bloqueo de dependencias de npm
│   ├── package.json              # Lista de dependencias y scripts del frontend
│   └── vite.config.js            # Configuración de Vite para el frontend
├── venv/                         # Entorno virtual de Python para el backend (ignorado en .gitignore)
├── .env                           # Variables de entorno para el backend
├── .gitignore                     # Ignora archivos innecesarios a nivel de proyecto
├── README.md                      # Documentación principal del proyecto
└── requirements.txt               # Lista de dependencias de Python
</pre>

## 🚀 Instalación y Configuración

<b> Prerrequisitos </br>
<b> Python 3.8+ </br>
<b> Node.js y npm (para el frontend en React) </br>
<b> Git (para clonar el repositorio) </br>

<h2>🔧 Configuración Inicial del Proyecto</h2>

- <h3>Haz un Fork del <a href="https://github.com/leopowerai/SecurityAI"><b>Repositorio</a></h3>
<ol>
  <li>Ve al repositorio original de <strong>SecureAI</strong> en GitHub.</li>
  <li>Haz clic en el botón <strong>Fork</strong> en la esquina superior derecha para crear una copia del repositorio en tu cuenta de GitHub.</li>
  <li>En tu cuenta de GitHub, ve a la página de tu fork del repositorio y copia la URL.</li>
</ol>

- <h3>Clona tu Fork del Repositorio</h3>

  <p>En tu terminal, clona el fork en tu máquina local:</p>
  <pre><code>git clone &lt;URL_DE_TU_FORK&gt;
  cd SecureAI</code></pre>

  <p>Reemplaza <code>&lt;URL_DE_TU_FORK&gt;</code> con la URL del repositorio de tu fork.</p>

- <h3>Configura el Backend</h3>

  a. Crear el Entorno Virtual
  <br>Para evitar conflictos con otras instalaciones de Python, crea un entorno virtual:
  <pre><code>python -m venv venv
  En Unix/macOS: source venv/bin/activate  # En Windows: ./venv/Scripts/activate</code></pre></br>

  b. Instala las Dependencias de Python
  <pre><code>pip install -r requirements.txt</code></pre>

  c. Crea el Archivo .env
  En la carpeta backend, crea un archivo .env con la URL de la base de datos y otras configuraciones:
  <pre><code>DATABASE_URL=sqlite:///./backend/database/test.db
  SECRET_KEY=tu_secreto
  ALGORITHM=HS256
  ACCESS_TOKEN_EXPIRE_MINUTES=30</code></pre>

  d. Inicializa la Base de Datos
  <pre><code>python backend/database/init_db.py</code></pre>

- <h3> Configura el Frontend </h3>
     a. Instala las Dependencias del Frontend
       <pre><code>cd frontend
       npm install</code></pre>
       
     b. Ejecuta el Servidor de Desarrollo de React
        <pre><code>npm start</code></pre>

## 🌐 Uso del Proyecto
En el directorio raíz, activa el entorno virtual y ejecuta el servidor FastAPI con Uvicorn:
<pre><code>uvicorn backend.app.main:app --reload</code></pre>

El backend estará disponible en http://127.0.0.1:8000.

Accede a la Documentación de la API
FastAPI proporciona una documentación interactiva que puedes ver en:

Swagger UI: http://127.0.0.1:8000/docs
<br>Redoc: http://127.0.0.1:8000/redoc</br>
<br>Accede al Frontend</br>
<br>Abre el navegador en http://localhost:3000 para acceder a la interfaz de usuario desarrollada en React.</br>

## 🧪 Pruebas
Ejecuta las pruebas automáticas para el backend usando pytest:

<pre><code>pytest backend/tests</code></pre>

Esto ejecutará las pruebas definidas en test_tasks.py y test_users.py y mostrará los resultados en la terminal.

<h2>🔧 Tecnologías y Herramientas</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a" />
  <img src="https://img.shields.io/badge/Code-JavaScript-informational?style=flat&logo=javascript&logoColor=white&color=2bbc8a" />
  <img src="https://img.shields.io/badge/Framework-React-informational?style=flat&logo=react&logoColor=white&color=61DAFB" />
  <img src="https://img.shields.io/badge/Framework-FastAPI-informational?style=flat&logo=fastapi&logoColor=white&color=009688" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-informational?style=flat&logo=postgresql&logoColor=white&color=336791" />
  <img src="https://img.shields.io/badge/Cloud-AWS-informational?style=flat&logo=amazon-aws&logoColor=white&color=FF9900" />
  <img src="https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=2496ED" />
</p>

<p>Para más información sobre cada lenguaje, puedes visitar la documentación correspondiente:</p>

<table>
  <thead align="center">
    <tr border: none;>
      <td><b>⚡ <a href="https://fastapi.tiangolo.com/learn/"><b>FastAPI</a></b></td>
      <td><b>⭐ <a href="https://es.react.dev/learn"><b>React</a></b></td>
      <td><b>📚 <a href="https://dev.java/learn/"><b>Java</a></b></td>
      <td><b>📉 <a href="https://dev.mysql.com/doc/"><b>SQL</a></b></td>
      <td><b>⛓️‍💥 <a href="https://developer.mozilla.org/en-US/docs/Web/HTML"><b>HTML</a></b></td>
      <td><b>🫥 <a href="https://developer.mozilla.org/en-US/docs/Web/CSS"><b>CSS</a></b></td>
    </tr>
  </thead>
  <tbody>  
  </tbody>
</table>
</ul>

<p></p>

<b></br>
<b></br>




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


<p align="center">
  🌱 En constante aprendizaje, explorando el desarrollo fullstack y la integración de <strong>inteligencia artificial</strong> y <strong>ciberseguridad</strong>.
</p>
