from flask import Blueprint , jsonify , abort , request
from .models import Account , User , Transaction , db
from werkzeug.security import generate_password_hash, check_password_hash
from .utils import unique_id


api_views = Blueprint('api_views' , __name__ , url_prefix='/api/')

@api_views.route('/')
def api_routes():
    return {
        'users':'api/users',
        'users by id':'api/users/<user_id>',
        'accounts':'api/accounts',
        'account by id':'api/account',
        'deposit funds':'transactions/deposit',
        'withdraw funds':'transactions/withdraw',
    }
    
#Users
@api_views.route('/users', methods = ['GET','POST'])
def get_all_users():
    if request.method == "GET":
        users = User.query.all()
        return jsonify([ account.to_dict() for account in users])
    else:
        pass
        #Implement create new user(Ayanda)

@api_views.route('/users/<user_id>' , methods = ['GET','DELETE'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404 , "User not found")
        return
    return jsonify(user.to_dict())
    

#Accounts
@api_views.route('/accounts' , methods = ['GET','POST'])
def get_all_accounts():
    if request.method == "GET":
        accounts = Account.query.all()
        return jsonify([ account.to_dict() for account in accounts])
    else:
        pass
        #Implement new account creation (Ayanda)
        """
            The client must send the user id to create the account with , if user id already has an account
            return 403 error , account already created
            if user id does not exist return 404 error
            otherwise create a new account
        """

@api_views.route('/accounts/<account_id>' , methods = ['GET' , 'PUT' , 'DELETE'])
def get_account(account_id):
    account = Account.query.get(account_id)
    if not account:
        abort(404 , "Account not found")
        return
    if request.method == "GET":
        return jsonify(account.to_dict())
    elif request.method == "PUT":
        #Update method (Thandeka)
        """
        The client must send their user id to validate request
        if user id does not exist return 404 error , user does not exist
        if user id exist but does not link with the current account return 403 error not authorised to update that account

        """
        pass
    
    else:
        #Delete method (Nokwanda)

        """
            The client must send the user id to validate that it is their account
            if the client fails to send user id or sends an user id that does not match account,
            return unauthorised 403 error abort(403 , "The mistake they made")
            if user id and account id link , delete the account not the user

        """
        pass

#Transactions(Sibusiso)
@api_views.route('/transactions/deposit' , methods = ['POST'])
def deposit():
    pass

@api_views.route('/transactions/withdraw' , methods = ['POST'])
def withdraw():
    pass

# @api_views.route('/transactions/transfer' , methods = ['POST'])
# def transfer():
#     #if there is time we can implement transafer
#     pass




# @api_views.route('/add-user')
# def add_user():
#     # new_hash = generate_password_hash('abc', method='bcrypt')
#     new_user = User(email="sbu12@gmail.com" , password_hash = "must hash me")
#     new_account = Account(first_name = "Sibusiso" , last_name = "Buthelezi" , balance=0 , id = '1234567890')
#     new_account.user = new_user
#     try:
#         db.session.add(new_user)
#         db.session.add(new_account)
#         db.session.commit()
#     except Exception as e:
#         return jsonify([{"Error":str(e)}])
#     else:
#         return jsonify([{"User":new_user , "Added":"Succesfully"}])