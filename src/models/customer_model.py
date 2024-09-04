from src.app import db

class Customer(db.Model):
    __tablename__='customers'
    customer_id= db.Column(db.String(5),primary_key=True,nullable=False)
    company_name=db.Column(db.String(100),nullable=False)
    contact_name=db.Column(db.String(100),nullable=False)
    contact_title=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=False)
    city=db.Column(db.String(100),nullable=False)
    region=db.Column(db.String(100))
    postal_code=db.Column(db.Integer,nullable=False)
    country=db.Column(db.String(100),nullable=False)
    phone=db.Column(db.String(100), unique=True,nullable=False)
    fax=db.Column(db.String(100),nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}