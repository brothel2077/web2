"""empty message

Revision ID: 383cb2876daa
Revises: 
Create Date: 2023-10-27 22:39:29.362870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '383cb2876daa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_books_cover_id_covers', 'books', type_='foreignkey')
    op.create_foreign_key(op.f('fk_books_cover_id_covers'), 'books', 'covers', ['cover_id'], ['id'], ondelete='CASCADE')
    op.drop_index('fk_books_has_genres_books_id_books', table_name='books_has_genres')
    op.drop_index('fk_books_has_genres_genres_id_genres', table_name='books_has_genres')
    op.create_foreign_key(op.f('fk_books_has_genres_genres_id_genres'), 'books_has_genres', 'genres', ['genres_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(op.f('fk_books_has_genres_books_id_books'), 'books_has_genres', 'books', ['books_id'], ['id'], ondelete='CASCADE')
    op.drop_index('fk_reviews_book_id_books', table_name='reviews')
    op.drop_index('fk_reviews_user_id_users', table_name='reviews')
    op.create_foreign_key(op.f('fk_reviews_user_id_users'), 'reviews', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(op.f('fk_reviews_book_id_books'), 'reviews', 'books', ['book_id'], ['id'], ondelete='CASCADE')
    op.drop_index('fk_users_role_id_roles', table_name='users')
    op.create_foreign_key(op.f('fk_users_role_id_roles'), 'users', 'roles', ['role_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_users_role_id_roles'), 'users', type_='foreignkey')
    op.create_index('fk_users_role_id_roles', 'users', ['role_id'], unique=False)
    op.drop_constraint(op.f('fk_reviews_book_id_books'), 'reviews', type_='foreignkey')
    op.drop_constraint(op.f('fk_reviews_user_id_users'), 'reviews', type_='foreignkey')
    op.create_index('fk_reviews_user_id_users', 'reviews', ['user_id'], unique=False)
    op.create_index('fk_reviews_book_id_books', 'reviews', ['book_id'], unique=False)
    op.drop_constraint(op.f('fk_books_has_genres_books_id_books'), 'books_has_genres', type_='foreignkey')
    op.drop_constraint(op.f('fk_books_has_genres_genres_id_genres'), 'books_has_genres', type_='foreignkey')
    op.create_index('fk_books_has_genres_genres_id_genres', 'books_has_genres', ['genres_id'], unique=False)
    op.create_index('fk_books_has_genres_books_id_books', 'books_has_genres', ['books_id'], unique=False)
    op.drop_constraint(op.f('fk_books_cover_id_covers'), 'books', type_='foreignkey')
    op.create_foreign_key('fk_books_cover_id_covers', 'books', 'covers', ['cover_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###
