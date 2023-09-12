from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    # serialize_rules = ('-bakeries.name',)
    # The above line would exclude the name attribute of the Bakery class from serialization. It is not needed in this context?
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    bakery = db.relationship('Bakery', backref='baked_goods')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


# SQLAlchemy-serializer is configured as a parameter in each of our models. The SeializerMixin param maps each attribute in the class to a python dict. This dict is then serialized (converted) to a json response (a list of objects).  