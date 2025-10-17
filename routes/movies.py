from fastapi import APIRouter, HTTPException
from database.db import collection_movies
from models.Movies import Movie, UpdateMovie
from bson import ObjectId

router = APIRouter(prefix="/movies", tags=["Movies"])
#obtener todas las peliculas
@router.get("/")
async def get_movies():
    movies = []
    async for doc in collection_movies.find({}):
        movies.append(Movie(**doc))
    return movies
#Insertar una pelicula
@router.post("/")
async def create_movie(movie: Movie):
    try:
        movie_dict = movie.dict(by_alias=True, exclude={"id"})

        new_film = await collection_movies.insert_one(movie_dict)
        film_created = await collection_movies.find_one({"_id": new_film.inserted_id})
        return Movie(**film_created)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear la película: {str(e)}")

#Obtener pelicula por nombre

@router.get("/title/{title}")
async def get_movie_by_title(title: str):
    movie = await collection_movies.find_one({"title": title})
    if not movie:
        raise HTTPException(status_code=404, detail="No se ha encontrado ninguna película con ese nombre")
    return Movie(**movie)