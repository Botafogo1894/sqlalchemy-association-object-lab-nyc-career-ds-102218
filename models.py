from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below
class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    songs = relationship('Song', back_populates = 'artist')
    genres = relationship('Genre', secondary='songs', back_populates='artists')

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    songs = relationship('Song', back_populates = 'genre')
    artists = relationship('Artist', secondary='songs')

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    artist_id = Column(String, ForeignKey('artists.id'))
    artist = relationship('Artist', back_populates = 'songs')
    genre_id = Column(String, ForeignKey('genres.id'))
    genre = relationship('Genre', back_populates = 'songs')


engine = create_engine('sqlite:///music.db')
Base.metadata.create_all(engine)
