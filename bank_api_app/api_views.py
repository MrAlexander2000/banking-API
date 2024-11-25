from flask import Blueprint , jsonify
from .models import Account , User , Transaction , db


api_views = Blueprint('api_views' , __name__ , url_prefix='/api/')

@api_views.route('/')
def home_api():
    return {"API Return":"Hello World"}

@api_views.route('/accounts')
def get_all_accounts():
    accounts = Account.query.all()
    return jsonify([ account.to_dict() for account in accounts])

@api_views.route('/users')
def get_all_users():
    accounts = User.query.all()
    return jsonify([ account.to_dict() for account in accounts])

@api_views.route('/add-user')
def add_user():
    new_user = User(email="abc@gmail.com" , password_hash = 'abc')
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({"Error":str(e)})
    else:
        return {"User":new_user , "Added":"Succesfully"}


