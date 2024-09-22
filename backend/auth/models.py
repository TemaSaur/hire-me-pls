from sqlalchemy import Column, Integer, String, LargeBinary, Boolean
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import uuid


class User(Base):
	__tablename__ = 'users'
	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	email = Column(String(255), unique=False, nullable=False)
	hashed_password = Column(LargeBinary, nullable=False)
	salt = Column(LargeBinary, nullable=False)
	is_organization = Column(Boolean, nullable=False, default=False)
