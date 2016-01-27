"""initial revision

Revision ID: 385836141ec8
Revises: 
Create Date: 2016-01-23 21:56:58.121713

"""

# revision identifiers, used by Alembic.
revision = '385836141ec8'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
            'tiles',
            sa.Column('id',sa.Integer,primary_key=True),
            sa.Column('description',sa.String(200),convert_unicode=True),
            )
    op.create_table(
            'players',
            sa.Column('id',sa.Integer,primary_key=True),
            sa.Column('user',sa.Integer,ForeignKey('users.id')),
            sa.Column('tile',sa.Integer,ForeignKey('tiles.id'))
            )


def downgrade():
    op.drop_table('tiles')
    op.drop_table('players')
