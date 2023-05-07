"""create earnings

Revision ID: 59cc92d0f31c
Revises: febb84b01d28
Create Date: 2023-05-03 21:12:25.626062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59cc92d0f31c'
down_revision = 'febb84b01d28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earnings_model',
    sa.Column('summa', sa.String(length=155), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('agent_source_id', sa.String(length=100), nullable=True),
    sa.Column('income_source_id', sa.String(length=100), nullable=True),
    sa.Column('is_other_source', sa.String(length=255), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['agent_source_id'], ['loan_admins.id'], ),
    sa.ForeignKeyConstraint(['income_source_id'], ['sources_of_income.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('earnings_model')
    # ### end Alembic commands ###
