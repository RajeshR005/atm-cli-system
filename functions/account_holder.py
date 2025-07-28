from createdb import db
from models import *
from utility import *


def account_holder_deposit(card_no):
    pin_no=input("Enter your PIN: ")
    user=check_auth(card_no,pin_no)
    if isinstance(user,str):
            print (user)
            continue_again()

    Add_cash(user)

