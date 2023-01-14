import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)