from flask import Blueprint , jsonify , abort , request , Response
from .models import Account , User , Transaction , db
from werkzeug.security import generate_password_hash, check_password_hash
from .utils import unique_id
from .exceptions import *
import json


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
        'transfer funds':'transactions/transfer',
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

@api_views.route('/users' , methods = ['POST'])
def create_user():
    pass

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
    data = request.get_json()
    status = transact(data , 'withdraw')
    if status == 'success':
        return Response(json.dumps({"success":"Amount deposited"}) , mimetype='application/json' , status=201)
    return status
    

@api_views.route('/transactions/withdraw' , methods = ['POST'])
def withdraw():
    data = request.get_json()
    status = transact(data , 'withdraw')
    if status == 'success':
        return Response(json.dumps({"success":"Amount Withdrawn"}) , mimetype='application/json' , status=201)
    return status

@api_views.route('/transactions/transfer' , methods = ['POST'])
def transfer():
    #if there is time we can implement transfer
    pass

def transact(data:dict , type):
    try:
        user = User.query.get(data['user_id'])
        if not user:
            raise NoUser
        account = Account.query.get(data['account_id'])
        if not account:
            raise NoAccount
        #verify user matches account
        if account.user_id != int(data['user_id']):
            raise User_and_Account
        for key in data:
            if key not in ['user_id' , 'account_id' , 'amount']:
                raise Exception
        return 'success'
        # return Response(json.dumps({"success":"Amount deposited"}) , mimetype='application/json' , status=201)
    except NoUser:
        return Response(json.dumps({"error":"User does not exist"}) , mimetype='application/json' , status=404)
    except NoAccount:
        return Response(json.dumps({"error":"Account does not exist"}) , mimetype='application/json' , status=404)
    except User_and_Account:
        return Response(json.dumps({"error":"current user is not authorised to deposit on this account"}) , mimetype='application/json' , status=403)
    except Exception as e:
        return Response(json.dumps({"error":f'Invalid Information expected {{"amount":"xxx" , "user_id":"xxx" , "account_id":"xxx"}} but got {data}"'}) , mimetype='application/json' , status=403)

