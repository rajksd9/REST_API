from src.app import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    category_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    category_name = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text)
    picture = db.Column(db.LargeBinary)  

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    