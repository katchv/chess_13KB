from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import *

from db import Base

class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)


