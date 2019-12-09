import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Entity(Base):
    __tablename__ = 'entities'

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime)
    title = Column(String)
    text = Column(String)
    rating = Column(Integer)
    voters_count = Column(Integer)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    def __init__(
            self,
            creation_date: datetime,
            title: str,
            category: str,
            text: str,
            rating: int,
            voters_count: int
    ):
        self.creation_date = creation_date
        self.title = title
        self.category = category
        self.text = text
        self.rating = rating,
        self.voters_count = voters_count

    def __repr__(self):
        return f'{self.title}'
