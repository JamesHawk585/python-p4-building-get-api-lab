from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    name = db.Column(db.String)
    bakery_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    # id = 
    name = db.Column(db.String)
    price = db.Column(db.Int)
    updated_at = db.Column(db.Boolean)


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    