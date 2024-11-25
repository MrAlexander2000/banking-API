class User_and_Account(Exception):
    #when user and account do not match
    pass

class NoUser(Exception):
    #when you do a query and a user is not found
    pass

class NoAccount(Exception):
    #when you do a query and an account is not found
    pass