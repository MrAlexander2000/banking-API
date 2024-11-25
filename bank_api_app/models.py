from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.sql import func
import os

app = Flask(__name__)
DB_NAME = 'banking.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(200))
    
    account = db.relationship('Account', back_populates='user', uselist=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password_hash": self.password_hash,  # Consider excluding sensitive data like password_hash in production
        }
    
    def __repr__(self):
        return f'{self.email}'
    
class Account(db.Model):
    
    __tablename__ = 'accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='account')
    
    transactions = db.relationship('Transaction', back_populates='account')
    
    def to_dict(self):
        return {
            "account_number":self.id,
            "balance": self.balance,
            "first_name": self.first_name,
            "last_name":self.last_name,
            "user_id":self.user_id
        }
    
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

class Transaction(db.Model):
    
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    account_id = db.Column(db.Integer , db.ForeignKey('accounts.id') , nullable=False)
    type = db.Column(Enum('withdraw' , 'deposit', name = 'transactions') , nullable = False)
    date = db.Column(db.DateTime(timezone=True) , server_default=func.now())
    account = db.relationship('Account', back_populates='transactions')
    
    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "type": self.type,
            "date":self.date,
            "account_id":self.account_id,
        }
    
    def __repr__(self):
        return f'{self.account.first_name} + {self.account.last_name} , {self.type}'
    

# class Transfer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     transaction_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False)
#     transaction = db.relationship('User' , backref='transactions')
#     to_account_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False)
#     to_account = db.relationship('Account' , backref='transactions')
    
#     def __repr__(self):
#         return f'{self.to_account.first_name} + {self.to_account.last_name}'
    
    
if __name__ == "__main__":
    if os.path.exists(DB_NAME.replace("sqlite://" , "")):
        print("Database already created")
    else:
        with app.app_context():
            db.create_all()
    