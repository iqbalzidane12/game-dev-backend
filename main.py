from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base
from app.models import user, game  # noqa: registers models with Base
from app.routers import auth, games
from seed import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed()
    yield


app = FastAPI(
    title="Mekan Games API",
    version="1.0.0",
    description="Backend API for the Mekan Games platform",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(games.router, prefix="/api/games", tags=["Games"])


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "Mekan Games API is running"}
