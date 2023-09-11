Tables have not yet been created. 

1. [] Create models in models.py
    - Include the relationship() SQLAlchemy method and SerializerMixin class. 
    - Direct Flask app to a db at app.db
2. [] Run migration with flask db revision --autogenerate -m'<my message>
3. [] Create a db file with flask db upgrade
4. [] Run seed.py 
5. [] Create four routes in app.py
    - GET /bakeries
    - GET /bakeries/<int:id>
    - GET /baked_goods_by_price
    - GET /baked_goods/most_expensive 