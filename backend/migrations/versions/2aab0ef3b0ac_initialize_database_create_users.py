"""Initialize database, create users

Revision ID: 2aab0ef3b0ac
Revises: 
Create Date: 2024-09-23 00:02:35.030722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '2aab0ef3b0ac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.LargeBinary(), nullable=False),
    sa.Column('salt', sa.LargeBinary(), nullable=False),
    sa.Column('is_organization', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('users')
