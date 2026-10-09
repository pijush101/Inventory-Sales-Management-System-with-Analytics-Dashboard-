from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{BASE_DIR / 'database' / 'greenleaf.db'}"
)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "greenleaf-dev-key-change-in-production")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
