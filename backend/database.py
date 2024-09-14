from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os

if __name__ == "__main__":
	import dotenv

	dotenv.load_dotenv("../.env")


DATABASE_URL = (
	f"postgresql+asyncpg://postgres:{os.getenv("PG_PASSWORD")}@localhost:5432/postgres"
)

engine = create_async_engine(DATABASE_URL)

async_session = async_sessionmaker(
	bind=engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_session():
	async with async_session() as session:
		yield session


class Item(Base):
	__tablename__ = "items"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	description = Column(String, index=True)


async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)


async def main():
	await init_db()


if __name__ == "__main__":
	import asyncio

	asyncio.run(main())
