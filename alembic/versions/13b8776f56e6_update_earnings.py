"""update earnings

Revision ID: 13b8776f56e6
Revises: 59cc92d0f31c
Create Date: 2023-05-03 22:15:50.227108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13b8776f56e6'
down_revision = '59cc92d0f31c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('earnings_model', sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('earnings_model', 'time_created')
    # ### end Alembic commands ###