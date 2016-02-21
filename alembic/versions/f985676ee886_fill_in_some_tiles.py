"""fill in some tiles

Revision ID: f985676ee886
Revises: 385836141ec8
Create Date: 2016-02-20 20:40:46.187783

"""

# revision identifiers, used by Alembic.
revision = 'f985676ee886'
down_revision = '385836141ec8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
	tiles = sa.Table('tiles',sa.MetaData())
	op.bulk_insert(tiles,[
			{"description":"This is the center of the world."},
			{"description":"A second place, not the center of the world"}]
		)


def downgrade():
    pass
