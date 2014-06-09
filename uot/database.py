"""USELESS. Just make some aliases for sqlite3.

Storeowner utilities.

Usage:

python database.py --add --title=X, --author=Y...
python database.py --remove record_id

"""

import argparse

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///records.db', echo=True)
    
Base = declarative_base()

Session = sessionmaker(bind=engine)

class Record(Base):
    __tablename__ = 'record'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    year = Column(Integer)
    thumbnail_url = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    
    def __init__(self, title, author, genre=None, year=None, thumbnail_url=None, description=None, quantity=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.thumbnail_url = thumbnail_url
        self.description = description
        self.quantity = quantity
        
    
    def __repr__(self):
        return "Album {}".format(self.title)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add&Remove records.')
    
    parser.add_argument('--add', action='store_true')
    parser.add_argument('--title')
    parser.add_argument('--author')
    parser.add_argument('--genre')
    parser.add_argument('--year')
    parser.add_argument('--thumb')
    parser.add_argument('--description')
    parser.add_argument('--quantity')
    parser.add_argument('--remove', action='store_true')
    
    args = parser.parse_args()
    
    #bello = Record()
    #session = Session()
    #session.add(bello)
    
    
    #voglio = session.query(Giorgio).filter_by(title='cock').first()
    #print(voglio)