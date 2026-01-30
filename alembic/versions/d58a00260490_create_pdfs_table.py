"""create pdfs table

Revision ID: d58a00260490
Revises: 8503fd8c1ddf
Create Date: 2026-01-18 21:22:33.753486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd58a00260490'
down_revision: Union[str, None] = '8503fd8c1ddf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
