from sqlalchemy import Column, Integer, String, Text

from api.core.database import Base


class Hero(Base):
    """Hero model for database.

    Attributes:
        id: Unique identifier
        name: Hero name
        alias: Hero alias/superhero name
        powers: Description of hero powers
    """

    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    alias = Column(String(100), unique=True, nullable=False, index=True)
    powers = Column(Text, nullable=True)
