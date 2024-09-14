import os
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy


jwt_strategy = JWTStrategy(
	secret=os.getenv("JWT_SECRET"),
	lifetime_seconds=60 * 60 * 24 * 30,
)

users = FastAPIUsers(
	
)
