from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from adapters.postgres_db import get_db
from repos.tvshows_repository import TVShowRepository

router = APIRouter(
    prefix="/tvshows",
    tags=["tvshows"]
)

@router.post("/")
async def create_tvshow(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    if "title" not in data or "genre" not in data:
        raise HTTPException(status_code=400, detail="Missing 'title' or 'genre'")
    
    tvshow = TVShowRepository.create_tvshow(db, data)
    return {
        "id": tvshow.id,
        "title": tvshow.title,
        "genre": tvshow.genre
    }

@router.get("/")
def list_tvshows(limit: int = 100, db: Session = Depends(get_db)):
    tvshows = TVShowRepository.get_tvshows(db, limit)
    return [
        {"id": tv.id, "title": tv.title, "genre": tv.genre}
        for tv in tvshows
    ]

@router.get("/{tvshow_id}")
def get_tvshow(tvshow_id: int, db: Session = Depends(get_db)):
    tvshow = TVShowRepository.get_tvshow_by_id(db, tvshow_id)
    if not tvshow:
        raise HTTPException(status_code=404, detail="TV Show not found")
    return {"id": tvshow.id, "title": tvshow.title, "genre": tvshow.genre}

@router.delete("/{tvshow_id}")
def delete_tvshow(tvshow_id: int, db: Session = Depends(get_db)):
    tvshow = TVShowRepository.delete_tvshow(db, tvshow_id)
    if not tvshow:
        raise HTTPException(status_code=404, detail="TV Show not found")
    return {"message": f"TV Show {tvshow_id} deleted"}
