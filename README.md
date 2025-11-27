# 🧩 SHORTER URL

Servicio desarrollado con **FastAPI** para gestionar URLs.  

---

## 🚀 Tecnologías principales

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python 3.13+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker-Compose](https://docs.docker.com/compose/)

---

## 💾 Esquema SQL

Se adjunta un archivo **schema.sql** que permite visualizar la estructura SQL de SQLite

---

## ⚙️ Variables de entorno

Las variables de entorno se cargan mediante el archivo `env.sh` **(Mac)**.  
Ejemplo de contenido:

```bash
export MYSQL_USER=root
export MYSQL_PASSWORD=password
export MYSQL_DB=shorturl
export MYSQL_HOST=localhost
```

Para cargarlas en tu entorno local **(Mac)**:

```bash
source env.sh
```

## ⚙️ Variables de entorno del contenedor levantado con docker-compose

Las variables de entorno que se utilizarán para el contenedor deben estar en un archivo `.env`.  
Ejemplo de contenido:

```bash
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DB=shorturl
MYSQL_HOST=localhost
```

---

## 🐳 Ejecución con Docker y/o Podman

### 1️⃣ Construir la imagen

```bash
docker build -t shorturl-image:1.0.0 .
podman build -t shorturl-image:1.0.0 .
```

### 2️⃣ Ejecutar el contenedor

```bash
docker run -d -p 8000:8000 --name shorturl-container --env-file ./.env shorturl-image:1.0.0
podman run -d -p 8000:8000 --name shorturl-container --env-file ./.env shorturl-image:1.0.0
```

> ⚠️ Nota: asegúrate de que el archivo `.env` esté en el mismo directorio donde ejecutas el comando `docker run`.

> **⚠️ Nota: se recomienda utilizar docker-compose**


### 3️⃣ Ejecución del docker-compose [All In One]

```bash
docker compose up -d --build [Levantar procesos]
podman compose up -d --build [Levantar procesos]

docker compose down -v [Kill procesos]
podman compose down -v [Kill procesos]
```

---

## ▶️ Ejecución local **(Mac)**

Crea un entorno virtual y activa las variables. Asegurate de tener python 3.13+:

```bash
python3.13.+ -m venv .venv
source .venv/bin/activate **usa .venv/bin/activate con powershell**
source env.sh
pip install -r requirements.txt
```

Ejecuta el servidor:

```bash
python src/main.py
```

---

## 📂 Estructura general del proyecto

```bash
short-url/
├── src/
│   ├── application/
│   │   ├── services/
│   │   ├── usecases/
│   ├── domain/
│   │   ├── dao/
│   │   ├── dto/
│   │   ├── exceptions/
│   │   ├── models/
│   │   ├── settings.py
│   ├── infrastructure/
│   │   ├── database/
│   │   ├── repositories/
│   │   ├── routes/
│   ├── container.py
│   ├── main.py
├── .env
├── env.sh
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── schema.sql
└── README.md
```

---

## 📜 Swagger del servicio

### Docs Endpoints REST

```bash
http://localhost:8000/docs
```

---

## ✨ Autor

**Kevin Espejel**  
📦 Proyecto interno: *🧩 SHORTER URL*