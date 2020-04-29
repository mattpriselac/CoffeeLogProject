"""add green_coffee table

Revision ID: 702662eca052
Revises: b542e63a6345
Create Date: 2020-04-29 11:05:29.623657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '702662eca052'
down_revision = 'b542e63a6345'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('green_coffee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('date_acquired', sa.String(length=10), nullable=True),
    sa.Column('origin_country', sa.String(length=30), nullable=True),
    sa.Column('farm_information', sa.String(length=140), nullable=True),
    sa.Column('official_notes', sa.String(length=140), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('green_coffee')
    # ### end Alembic commands ###