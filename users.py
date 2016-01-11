from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy import func
import datetime
from database import Base

class Galluser(Base):
    """ Implements all the stuff flask-auth wants etc etc"""
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    username = Column(String(255),unique=True)
    created = Column(DateTime,server_default=func.now())
    email = Column(String(255),unique=True)
    nonce = Column(String(64))
    hash = Column(String(64))



    def __init__(self,
                username=None,
                email=None,
                nonce=None,
                hash = None,):
        self.username = username
        self.email = email
        self.nonce = nonce
        self.hash = hash

    def __repr__(self):
        return '<User %r>'%(self.id)

    def is_authenticated(self):
        return True

    def is_active (self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return u"%s"%self.id




