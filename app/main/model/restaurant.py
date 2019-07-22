from app.main import db
from  sqlalchemy.sql.expression import func

class Restaurant(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __eq__(self, other):
        return self.name == other.name and self.address == other.address

    def __repr__(self):
        return repr('Restaurant {}'.format(self.name))