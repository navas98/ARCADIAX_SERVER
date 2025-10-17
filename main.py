from fastapi import FastAPI
app=FastAPI()

#Crear la aplicacion de fastAPI
app=FastAPI(
    title="ArcadiaX API",
    description="API para gestionar videojuegos, peliculas y dispositivos",
    version="1.0.0"
)
@app.get("/ping")
def ping():
    return{"mensaje":"pong"}

#lanzar el proyecto:
# python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000