"""create source of income

Revision ID: febb84b01d28
Revises: b39cbc8a5794
Create Date: 2023-05-03 20:04:43.319256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'febb84b01d28'
down_revision = 'b39cbc8a5794'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sources_of_income',
    sa.Column('source', sa.String(length=100), nullable=False),
    sa.Column('agent_source_id', sa.String(length=100), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['agent_source_id'], ['loan_admins.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sources_of_income')
    # ### end Alembic commands ###
