import uuid
from sqlalchemy import Column, String, Float, Integer
from app.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True, default=lambda: f"game_{uuid.uuid4().hex[:8]}")
    title = Column(String, nullable=False, index=True)
    description = Column(String, default="")
    thumbnail = Column(String, default="")
    genre = Column(String, default="", index=True)
    rating = Column(Float, default=0.0)
    player_count = Column(Integer, default=0)
    gradient = Column(String, default="")
