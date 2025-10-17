from fastapi import FastAPI
from database.db import db
app=FastAPI()

#Crear la aplicacion de fastAPI
app=FastAPI(
    title="ArcadiaX API",
    description="API para gestionar videojuegos, peliculas y dispositivos",
    version="1.0.0"
)

@app.on_event("startup")
async def check():
    try:
        await db.command("ping")
        print("Mongo db conectada")
    except Exception as e:
        print("Mongo db no conectado",e)

@app.get("/ping")
def ping():
    return{"mensaje":"pong"}

#lanzar el proyecto:
# python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000