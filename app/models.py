from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    dataCreated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    afastado = db.Column(db.Boolean, default=False)
    dataDispensa = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'
