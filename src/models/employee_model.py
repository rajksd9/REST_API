from src.app import db

class Employee(db.Model):
    __tablename__ = "employees"

    employee_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(30))
    title_of_courtesy = db.Column(db.String(25))
    birth_date = db.Column(db.Date)
    hire_date = db.Column(db.Date)
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    home_phone = db.Column(db.String(24))
    extension = db.Column(db.String(4))
    photo = db.Column(db.LargeBinary)  
    notes = db.Column(db.Text)
    reports_to = db.Column(db.SmallInteger, db.ForeignKey('employees.employee_id'))
    photo_path = db.Column(db.String(255))

   
    reports_to_employee = db.relationship('Employee', remote_side=employee_id, backref='subordinates')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
