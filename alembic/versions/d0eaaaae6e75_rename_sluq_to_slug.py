"""rename sluq to slug

Revision ID: d0eaaaae6e75
Revises: 9ebee55f44bc
Create Date: 2026-11-16 18:03:55.525466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd0eaaaae6e75'
down_revision: Union[str, Sequence[str], None] = '9ebee55f44bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("projects", "sluq", new_column_name="slug")


def downgrade() -> None:
    op.alter_column("projects", "slug", new_column_name="sluq")