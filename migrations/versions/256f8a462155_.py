"""empty message

Revision ID: 256f8a462155
Revises: cb8e39205df1
Create Date: 2019-11-21 08:59:43.377780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '256f8a462155'
down_revision = 'cb8e39205df1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reclamacao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=True),
    sa.Column('local', sa.String(length=100), nullable=True),
    sa.Column('tempo', sa.String(length=50), nullable=True),
    sa.Column('desc', sa.String(length=500), nullable=True),
    sa.Column('img_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reclamacao')
    # ### end Alembic commands ###
