from src.app import db

class Supplier(db.Model):
    __tablename__="suppliers"
    supplier_id=db.Column(db.SmallInteger, primary_key=True, nullable=False)
    company_name=db.column(db.String(40))
    contact_name= db.Column(db.String(30))
    contact_title=db.Column(db.String(30))
    address=db.Column(db.String(60))
    city=db.Column(db.String(15))
    region=db.Column(db.String(15))
    postal_code=db.Column(db.String(10))
    country=db.Column(db.String(15))
    phone=db.Column(db.String(24))
    fax=db.Column(db.String(24))
    homepage=db.Column(db.Text())

    
    def as_dict(self):
        return {c.name:getattr(self,c.name) for c in self.__table__.columns}