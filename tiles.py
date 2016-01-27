from database import Base
from sqlalchemy import Column,Integer,String



class Tile(Base):
    __tablename__='tiles'
    id = Column(Integer,primary_key=True)
    description = Column(String(200))


    def __init__(self,
            id = None,
            description = None):
        self.id = id
        self.description = u""

    def __repr__(self):
        return "<Tile %r>"%self.id

class Player(Base):
    __tablename__='players'
    id = Column(Integer,primary_key=True)
    description = Column(String(200))

    def __init__(self,
            id = None,
            description = None):
        self.id=id
        self.description = description

    def __repr__(self):
        return "<Player %r>"%self.id

