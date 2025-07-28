from adapters.postgres_db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    author = Column(String)


class TVShow(Base):
    __tablename__ = "tvshows"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    author = Column(String)