from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
    
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
    tracklist = Array(Unicode)
    
    def __repr__(self):
        return "Album {}".format(self.title)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    bello = Record()
    session = Session()
    session.add(bello)
    
    
    voglio = session.query(Giorgio).filter_by(title='cock').first()
    print(voglio)

def add_record(): pass

def populate():
    db.create_all()
    maligno = Record(author='Capro', title='Maligno',genre='Sludge')
    badthings = Record(author='Carcione', title='Bad Things',genre='Blues')
    db.session.add(maligno)
    db.session.add(badthings)
    db.session.flush()
    db.session.commit()