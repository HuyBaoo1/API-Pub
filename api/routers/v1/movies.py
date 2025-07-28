from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from adapters.postgres_db import get_db
from repos.movies_repository import MovieRepository

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)

@router.post("/")
async def create_movie(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    if "title" not in data or "genre" not in data:
        raise HTTPException(status_code=400, detail="Missing 'title' or 'genre'")
    
    movie = MovieRepository.create_movie(db, data)
    return {
        "id": movie.id,
        "title": movie.title,
        "genre": movie.genre
    }

@router.get("/")
def list_movies(limit: int = 100, db: Session = Depends(get_db)):
    movies = MovieRepository.get_movies(db, limit)
    return [
        {"id": m.id, "title": m.title, "genre": m.genre}
        for m in movies
    ]

@router.get("/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = MovieRepository.get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"id": movie.id, "title": movie.title, "genre": movie.genre}

@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = MovieRepository.delete_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": f"Movie {movie_id} deleted"}
