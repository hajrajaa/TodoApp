"""Create phone number for user column

Revision ID: 17030b3f57da
Revises: 
Create Date: 2026-02-25 16:57:02.690575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17030b3f57da'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))



def downgrade() -> None:
    op.drop_column('users', 'phone_number')

