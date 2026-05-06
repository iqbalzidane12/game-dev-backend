"""Seed the database with sample games and a default admin user."""
from app.database import engine, SessionLocal, Base
from app.models import user, game  # noqa: register models
from app.models.user import User
from app.models.game import Game
from app.core.security import hash_password

Base.metadata.create_all(bind=engine)

GAMES = [
    {
        "id": "game_colorsort",
        "title": "Color Sort",
        "description": "Sort colored balls into matching tubes. A relaxing puzzle that challenges your logic and patience.",
        "thumbnail": "/images/color-sort.png",
        "genre": "Puzzle",
        "rating": 4.5,
        "player_count": 12840,
        "gradient": "from-pink-500 to-purple-600",
    },
    {
        "id": "game_escape",
        "title": "Escape",
        "description": "Find clues, solve riddles, and break out before time runs out in this thrilling escape room.",
        "thumbnail": "/images/escape.png",
        "genre": "Adventure",
        "rating": 4.7,
        "player_count": 9320,
        "gradient": "from-yellow-500 to-orange-600",
    },
    {
        "id": "game_numberlink",
        "title": "Number Link",
        "description": "Connect matching numbers with paths that fill the entire grid without crossing each other.",
        "thumbnail": "/images/number-link.png",
        "genre": "Puzzle",
        "rating": 4.3,
        "player_count": 7450,
        "gradient": "from-blue-500 to-cyan-600",
    },
    {
        "id": "game_paint",
        "title": "Paint",
        "description": "Express your creativity with a full digital canvas. Draw, paint, and share your artwork.",
        "thumbnail": "/images/paint.png",
        "genre": "Creative",
        "rating": 4.1,
        "player_count": 5210,
        "gradient": "from-green-400 to-teal-500",
    },
    {
        "id": "game_sudoku",
        "title": "Sudoku",
        "description": "The classic number placement puzzle. Fill the 9x9 grid so every row, column, and box contains 1–9.",
        "thumbnail": "/images/sudoku.png",
        "genre": "Puzzle",
        "rating": 4.8,
        "player_count": 21500,
        "gradient": "from-indigo-500 to-violet-600",
    },
    {
        "id": "game_chess",
        "title": "Chess",
        "description": "Challenge opponents in the ultimate strategy game. Master openings, tactics, and endgames.",
        "thumbnail": "/images/chess.png",
        "genre": "Strategy",
        "rating": 4.9,
        "player_count": 34100,
        "gradient": "from-gray-600 to-gray-900",
    },
    {
        "id": "game_2048",
        "title": "2048",
        "description": "Slide numbered tiles to combine them and reach the elusive 2048 tile.",
        "thumbnail": "/images/2048.png",
        "genre": "Puzzle",
        "rating": 4.4,
        "player_count": 18700,
        "gradient": "from-amber-400 to-orange-500",
    },
    {
        "id": "game_snake",
        "title": "Snake",
        "description": "Guide the snake to eat food and grow longer without hitting the walls or yourself.",
        "thumbnail": "/images/snake.png",
        "genre": "Arcade",
        "rating": 4.2,
        "player_count": 15300,
        "gradient": "from-lime-500 to-green-600",
    },
]

ADMIN_USER = {
    "id": "usr_admin01",
    "email": "admin@mekangames.com",
    "name": "Admin",
    "password": "password123",
    "avatar": "",
}


def seed():
    db = SessionLocal()
    try:
        # Seed games
        for data in GAMES:
            if not db.query(Game).filter(Game.id == data["id"]).first():
                db.add(Game(**data))
                print(f"  + Game: {data['title']}")
            else:
                print(f"  ~ Game already exists: {data['title']}")

        # Seed admin user
        if not db.query(User).filter(User.email == ADMIN_USER["email"]).first():
            db.add(User(
                id=ADMIN_USER["id"],
                email=ADMIN_USER["email"],
                name=ADMIN_USER["name"],
                avatar=ADMIN_USER["avatar"],
                password_hash=hash_password(ADMIN_USER["password"]),
            ))
            print(f"  + User: {ADMIN_USER['email']}")
        else:
            print(f"  ~ User already exists: {ADMIN_USER['email']}")

        db.commit()
        print("\nSeeding complete.")
    finally:
        db.close()


if __name__ == "__main__":
    print("Seeding database...")
    seed()
