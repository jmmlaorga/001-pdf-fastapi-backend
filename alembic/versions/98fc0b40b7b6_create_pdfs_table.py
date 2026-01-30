"""create pdfs table

Revision ID: 98fc0b40b7b6
Revises: d58a00260490
Create Date: 2026-01-18 21:28:46.743634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98fc0b40b7b6'
down_revision: Union[str, None] = 'd58a00260490'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
