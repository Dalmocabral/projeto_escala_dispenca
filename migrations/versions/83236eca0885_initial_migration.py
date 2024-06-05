"""Initial migration.

Revision ID: 83236eca0885
Revises: d20d8bd7b89d
Create Date: 2024-06-04 11:25:16.482773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83236eca0885'
down_revision = 'd20d8bd7b89d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dataDispensa', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('dataDispensa')

    # ### end Alembic commands ###