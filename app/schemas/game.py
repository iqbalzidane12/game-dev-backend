from pydantic import BaseModel, Field


class GameResponse(BaseModel):
    id: str
    title: str
    description: str
    thumbnail: str
    genre: str
    rating: float
    playerCount: int = Field(validation_alias="player_count")
    gradient: str

    model_config = {"from_attributes": True, "populate_by_name": True}


class GameCreate(BaseModel):
    title: str
    description: str = ""
    thumbnail: str = ""
    genre: str = ""
    rating: float = 0.0
    playerCount: int = 0
    gradient: str = ""
