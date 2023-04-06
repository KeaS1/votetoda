"""init

Revision ID: 6e890199fd2b
Revises: 
Create Date: 2023-03-17 11:04:03.937592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e890199fd2b'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'Customers',
        sa.Column('customers_id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('second_name', sa.String, nullable=False),
        sa.Column('addresses', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('Customers')