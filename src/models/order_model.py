from src.app import db
from src.models.shipper_model import Shipper
from src.models.customer_model import Customer
from src.models.employee_model import Employee

class Order(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    customer_id = db.Column(db.String(5), db.ForeignKey('customers.customer_id'))
    employee_id = db.Column(db.SmallInteger, db.ForeignKey('employees.employee_id'))
    order_date = db.Column(db.Date)
    required_date = db.Column(db.Date)
    shipped_date = db.Column(db.Date)
    ship_via = db.Column(db.SmallInteger, db.ForeignKey('shippers.shipper_id'))
    freight = db.Column(db.Numeric(10, 2))
    ship_name = db.Column(db.String(40))
    ship_address = db.Column(db.String(60))
    ship_city = db.Column(db.String(15))
    ship_region = db.Column(db.String(15))
    ship_postal_code = db.Column(db.String(10))
    ship_country = db.Column(db.String(15))

    # Define relationships
    customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))
    employee = db.relationship("Employee", backref=db.backref('orders', lazy=True))
    shipper = db.relationship("Shipper", backref=db.backref('orders', lazy=True))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
