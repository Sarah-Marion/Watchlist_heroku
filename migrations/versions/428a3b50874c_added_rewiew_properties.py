"""added rewiew properties

Revision ID: 428a3b50874c
Revises: 99e765f994f2
Create Date: 2018-05-17 12:05:37.359660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '428a3b50874c'
down_revision = '99e765f994f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('movie_title', sa.String(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('movie_review', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    op.drop_table('reviews')
    # ### end Alembic commands ###
