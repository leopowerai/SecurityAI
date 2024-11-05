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
       El frontend estará disponible en http://localhost:3000.
       
     b. Ejecuta el Servidor de Desarrollo de React
        <pre><code>npm start</code></pre>

- <H3>Crear la Base de Datos</h3>
      Ejecuta el script de inicialización para crear la base de datos test.db y sus tablas:
      <pre><code>python -m Backend.database.init_db</code></pre>

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

Desactivación del Entorno Virtual: Cuando termines de trabajar en el proyecto, puedes desactivar el entorno virtual con:

<pre><code>deactivate</code></pre>

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






<p align="center">
  🌱 En constante aprendizaje, explorando el desarrollo fullstack y la integración de <strong>inteligencia artificial</strong> y <strong>ciberseguridad</strong>.
</p>
