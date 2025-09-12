from fastapi import FastAPI
from fastapi.responses import RedirectResponse, FileResponse
from . import models, database, routes
import os

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

# Initialize app
app = FastAPI(title="Weather API")

# Include your CRUD routes
app.include_router(routes.router)

# Redirect root '/' to Swagger UI
@app.get("/")
def root():
    return RedirectResponse(url="/docs")

# Serve favicon to avoid 404 logs
@app.get("/favicon.ico")
def favicon():
    favicon_path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return FileResponse(os.devnull)  # empty file if favicon doesn't exist
