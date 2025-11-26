"""Create matakuliah table

Revision ID: d3a9c62440bb
Revises: 
Create Date: 2025-11-26 15:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a9c62440bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('matakuliah',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('kode_mk', sa.Text(), nullable=False),
        sa.Column('nama_mk', sa.Text(), nullable=False),
        sa.Column('sks', sa.Integer(), nullable=False),
        sa.Column('semester', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('kode_mk')
    )


def downgrade():
    op.drop_table('matakuliah')
