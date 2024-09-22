from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

import dotenv
dotenv.load_dotenv("../.env")


DATABASE_URL = "postgresql://postgres:{}@0.0.0.0:5432/postgres"\
		.format(os.getenv("PG_PASSWORD"))

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
