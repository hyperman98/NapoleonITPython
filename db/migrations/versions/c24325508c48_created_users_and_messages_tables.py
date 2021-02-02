"""Created Users and Messages tables

Revision ID: c24325508c48
Revises: 
Create Date: 2021-01-30 03:51:23.540043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c24325508c48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('message', sa.String(length=100), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('sent_messages', sa.Integer(), nullable=True),
    sa.Column('received_messages', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('login')
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('messages')
