from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///music.db')

Session = sessionmaker(bind=engine)
session = Session()

def query_all_songs_band(bandname):
    return session.query(Artist).filter(Artist.name == bandname).first().songs
    # import pdb; pdb.set_trace()
def genre_of_all_songs_by_artist(bandname):
    song_list = session.query(Artist).filter(Artist.name == bandname).first().songs
    genres =  [item.genre for item in song_list]
    return [item.name for item in genres]
