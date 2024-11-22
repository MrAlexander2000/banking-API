from flask_sqlachemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Interger , primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    surname = db.Column(db.String(100) , nullable=False)
    email = db.Column(db.String(100) , nullable=False , unique=True)
    
    def __str__(self):
        return f"{self.name} + {self.surname}"
    