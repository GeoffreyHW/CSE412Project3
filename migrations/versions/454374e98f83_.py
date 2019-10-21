"""empty message

Revision ID: 454374e98f83
Revises: ffacc65ed722
Create Date: 2018-04-26 01:19:19.038934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '454374e98f83'
down_revision = 'ffacc65ed722'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('query5')
    op.drop_table('query9')
    op.drop_table('query7')
    op.drop_table('query3')
    op.drop_table('query2')
    op.drop_table('query8')
    op.drop_table('query1')
    op.drop_table('query10')
    op.drop_table('query6')
    op.drop_table('query4')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('query4',
    sa.Column('movieid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_table('query6',
    sa.Column('average', sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    op.create_table('query10',
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_table('query1',
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('moviecount', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    op.create_table('query8',
    sa.Column('average', sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    op.create_table('query2',
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    op.create_table('query3',
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('countofratings', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    op.create_table('query7',
    sa.Column('average', sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    op.create_table('query9',
    sa.Column('movieid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    op.create_table('query5',
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('average', sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###