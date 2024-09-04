from src.app import db
class Shipper(db.Model):
    __tablename__="shippers"
    shipper_id=db.Column(db.SmallInteger, primary_key=True)
    company_name=db.Column(db.String(40),nullable=False)
    phone=db.Column(db.String(24))

    def as_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}



