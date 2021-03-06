from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from gallertoid import app


engine = create_engine(app.config['SQL_ALCHEMY_DATABASE_URI']+'gallertoid')
#  Connection URL: mysql://$OPENSHIFT_MYSQL_DB_HOST:$OPENSHIFT_MYSQL_DB_PORT/
#mysql://adminsX4kPYt:lmX8jFYZpEVj@localhost/gallertoid")
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    #import all model classes here
    import users
    import tiles
    Base.metadata.create_all(bind=engine)
