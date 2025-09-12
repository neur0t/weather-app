# Weather App 🌤️ (FastAPI + SQLite)

A simple Weather API built with **FastAPI**, **SQLite**, and **Dockerized** for deployment.  
Implements CRUD operations for weather station measurements.

## Features
- Add new weather measurements
- Retrieve measurements (filter by date & station)
- Update measurement values
- Basic token authentication
- SQLite database for storage
- OpenAPI/Swagger documentation auto-generated

## Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Docker](https://www.docker.com/)

## Run Locally

```bash
# Clone repo
git clone https://github.com/<your-username>/weather-app.git
cd weather-app

# Install dependencies
pip install -r requirements.txt

# Run app
uvicorn app.main:app --reload

#Run with Docker
docker build -t weather-app .
docker run -p 8000:8000 weather-app
redirected to /docs



!!!!!!!!!!!!Those endpoints need authantication from a Token!!!!!!!!!!!!!!!!!!!
If I gave you the Token, you can authenticate yourself at /docs
and use the API 