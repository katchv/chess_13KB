from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.orm.session import *
from sqlalchemy.orm.exc import *

from config import config


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

Base = declarative_base(metadata=MetaData(naming_convention=convention))

def get_db_url(config):
    dbname = config["database"].get("name")
    user = config["database"].get("user")
    password = ":" + config["database"].get("password")
    host = config["database"].get("host", "localhost")
    port = config["database"].getint("port", 5432)

    url = "postgresql://{user}{password}@{host}:{port}/{dbname}".format(user=user, password=password, host=host, dbname=dbname, port=port)

    return url

def init_session():
    engine = create_engine(get_db_url(config), echo=config['application'].getboolean("debug", False))

    Session = sessionmaker()
    Session.configure(bind=engine, autoflush=False, autocommit=False)

    return Session()

session = init_session()
