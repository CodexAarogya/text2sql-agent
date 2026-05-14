from sqlalchemy import create_engine
from dotenv import load_dotenv
from app.settings import settings

load_dotenv("../.env")

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(
    url=DATABASE_URL,
    echo=True
)

