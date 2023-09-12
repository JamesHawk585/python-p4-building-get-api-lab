"""changes bakery_id in BakedGood model

Revision ID: fcfb63a54603
Revises: 58efecabe51c
Create Date: 2023-09-11 20:16:13.770611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcfb63a54603'
down_revision = '58efecabe51c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bakery_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_baked_goods_bakery_id_bakeries'), 'bakeries', ['bakery_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_baked_goods_bakery_id_bakeries'), type_='foreignkey')
        batch_op.drop_column('bakery_id')

    # ### end Alembic commands ###