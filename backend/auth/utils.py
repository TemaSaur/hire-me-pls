from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users import BaseUserManager

from backend.auth.models import User


async def get_user_manager(session: AsyncSession):
	yield BaseUserManager(session, User, get_password_hash)