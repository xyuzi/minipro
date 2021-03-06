"""empty message

Revision ID: 55a81012960d
Revises: 
Create Date: 2020-11-07 22:22:33.500614

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '55a81012960d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('channel_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=130), nullable=True),
    sa.Column('cover', sa.String(length=130), nullable=True),
    sa.Column('ctime', mysql.DATETIME(fsp=3), nullable=True),
    sa.Column('comment_count', sa.Integer(), nullable=True),
    sa.Column('text', sa.TEXT(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('channel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile', sa.String(length=11), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('article_count', sa.Integer(), nullable=True),
    sa.Column('profile_photo', sa.String(length=130), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('channel')
    op.drop_table('article')
    # ### end Alembic commands ###
