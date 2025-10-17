from fastapi import FastAPI
from database.db import db
from routes import movies
app=FastAPI()

#Crear la aplicacion de fastAPI
app=FastAPI(
    title="ArcadiaX API",
    description="API para gestionar videojuegos, peliculas y dispositivos",
    version="1.0.0"
)
app.include_router(movies.router)

@app.get("/ping")
def ping():
    return{"mensaje":"pong"}

#lanzar el proyecto:
# python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000