from fastapi import FastAPI
from api.routers.v1 import users, movies, tvshows
from adapters.postgres_db import engine
from models.postgres import Base


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Streaming App API",
    version="1.0.0"
)


app.include_router(users.router)
app.include_router(movies.router)
app.include_router(tvshows.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Streaming App API!"}
