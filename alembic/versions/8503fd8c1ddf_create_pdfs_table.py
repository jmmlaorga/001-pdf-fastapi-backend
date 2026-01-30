"""create pdfs table

Revision ID: 8503fd8c1ddf
Revises: 30a84d438097
Create Date: 2026-01-18 20:08:47.966647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8503fd8c1ddf'
down_revision: Union[str, None] = '30a84d438097'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
