from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    route = Column(String)
    title = Column(String)
    image = Column(String)

    entities = relationship("Entity", back_populates="categories")

    def __init__(
            self,
            route: str,
            title: str,
            image: str
    ):
        self.route = route
        self.title = title
        self.image = image

    def __repr__(self):
        return f'<Category>' \
            f'{self.title} '
