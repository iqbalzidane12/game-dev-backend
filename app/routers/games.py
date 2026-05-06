from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.game import Game
from app.models.user import User
from app.schemas.game import GameResponse
from app.core.deps import get_current_user


router = APIRouter()


@router.get("", response_model=List[GameResponse])
def get_games(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return db.query(Game).all()


# /search must come before /{game_id} so it isn't captured as a path param
@router.get("/search", response_model=List[GameResponse])
def search_games(
    q: str = Query(..., min_length=1, description="Search by title or genre"),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    term = f"%{q}%"
    return (
        db.query(Game)
        .filter(Game.title.ilike(term) | Game.genre.ilike(term))
        .all()
    )


@router.get("/{game_id}", response_model=GameResponse)
def get_game(
    game_id: str,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game
