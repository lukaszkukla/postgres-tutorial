from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the 'chinook' database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for session
# create a new instance of sessionmaker, then point to our enging (db)
Session = sessionmaker(db)

# open an actual session by calling Session() subclass defined above
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the 'Artist' table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select Name from the 'Artist' table

# Query 3 - select Queen from the 'Artist' table

# Query 4 - select ArtistId #51 from the 'Artist' table

# Query 5 - select all albums for ArtistId #51 from the 'Album' table

# Query 6 - select all tracks where composer is 'Queen' from the 'Track' table
