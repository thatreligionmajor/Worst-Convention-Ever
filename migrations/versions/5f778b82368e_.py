"""empty message

Revision ID: 5f778b82368e
Revises: 8b37094d23cf
Create Date: 2023-10-04 16:36:51.777064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f778b82368e'
down_revision = '8b37094d23cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Magic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('magic_id', sa.Integer(), nullable=False),
    sa.Column('magic_name', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['magic_id'], ['Magic.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('login_method', sa.String(length=80), nullable=True))
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=False))
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('phone')
        batch_op.drop_column('login_method')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    op.drop_table('Favorites')
    op.drop_table('Magic')
    # ### end Alembic commands ###
