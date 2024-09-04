# from database.init_db import get_db_connection
# import psycopg2
# import psycopg2.extras
# import json

# class product_model():

#     def __init__(self):
#         try:
#             self.conn=get_db_connection()
#             self.cur=self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
#         except:
#             print ("data")


#     def getAllProducts(self):
#         try:
#             self.cur.execute("Select * from Products;")
#             result = self.cur.fetchall()
#             print(result)
#             return json.dumps(result)
#         except:
#             return ({
#                 "message":"Error fetching data"
#             })
        
        
        
from src.app import db
from src.models.category_model import Category
from src.models.supplier_model import Supplier

class Product(db.Model):
    __tablename__ = 'products'
    
    product_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    product_name = db.Column(db.String(40), nullable=False)
    supplier_id = db.Column(db.SmallInteger, db.ForeignKey('suppliers.supplier_id'))
    category_id = db.Column(db.SmallInteger, db.ForeignKey('categories.category_id'))
    quantity_per_unit = db.Column(db.String(20))
    unit_price = db.Column(db.Numeric(10, 2))
    units_in_stock = db.Column(db.SmallInteger)
    units_on_order = db.Column(db.SmallInteger)
    reorder_level = db.Column(db.SmallInteger)
    discontinued = db.Column(db.SmallInteger, nullable=False)
    
    category = db.relationship('Category', backref=db.backref('products', lazy=True))
    supplier = db.relationship('Supplier', backref=db.backref('products', lazy=True))
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
