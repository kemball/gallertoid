from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey



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
    tile = Column(Integer, ForeignKey("tiles.id"),nullable=False)
    user = Column(Integer,ForeignKey("users.id"),nullable=False)

    def __init__(self,
            tile = None,
            user = None):
        self.tile = tile
        self.user = user

    def __repr__(self):
        return "<Player %r>"%self.id

