"""empty message

Revision ID: 755e8cb9a022
Revises: 
Create Date: 2023-05-19 12:40:16.012759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '755e8cb9a022'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('resumo', sa.String(length=100), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conta')
    # ### end Alembic commands ###
