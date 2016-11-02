from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *

from db import Base

class Figure(Base):
    __tablename__ = "figure"

    id = Column(Integer, primary_key=True)
    type = Column(CHAR, nullable=False)
    col = Column(Integer, default=0)
    row = Column(Integer, default=0)
    color = Column(Text)
    killed = Column(Boolean)

    board_id = Column(Integer, ForeignKey("board.id"), nullable=False)
    board = relationship("Board", backref="figures")

    def __str__(self):
        return self.type
