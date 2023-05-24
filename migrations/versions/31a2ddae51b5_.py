"""empty message

Revision ID: 31a2ddae51b5
Revises: 350d8c01a685
Create Date: 2023-05-23 16:19:34.517373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31a2ddae51b5'
down_revision = '350d8c01a685'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conta', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'conta', 'usuario', ['usuario_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'conta', type_='foreignkey')
    op.drop_column('conta', 'usuario_id')
    # ### end Alembic commands ###
