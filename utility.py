#Password Hashing
from passlib.context import CryptContext
from createdb import db
from models import *


pwd=CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pin(pin):
    return pwd.hash(pin)

def verify_pin(pin,hash_pin):
    return pwd.verify(pin,hash_pin)

#--------------------------------------------------

#verify User's

def check_auth(card_no,pin):
    user=db.query(Accountinfo).filter(Accountinfo.atm_card_no==card_no).first()
    if not user:
        return("Invalid Credentials")
    pin=verify_pin(pin,user.pin_no)
    if not pin:
        return("Invalid Credentials")
    get_user=db.query(User).filter(User.id==user.user_id).first()
    return get_user



#----------------------------------------------------------------

#Retrun user Details:

def user_details(user_id):
    get_user=db.query(User,Accountinfo).join(User.account_user).filter(User.id==user_id,Accountinfo.user_id==user_id).first()

    return{
        "msg":"User Detailed Saved Sucessfully",
        "Name":get_user[0].name,
        "Phone No":get_user[0].phone_num,
        "Account No":get_user[1].Account_no,
        "Card No":get_user[1].atm_card_no,
        "Available Balance":get_user[1].avail_balance
    }


#------------------------------------------------------------------------------

def continue_again():
    print("\nIf you want to \
          \nVisit Menu's = 1\
          \nExit = 2")
    user_choice=int(input("\nEnter Your choice: "))
    if user_choice==1:
        from menu_atm import menus
        menus()
    elif user_choice==2:
        exit()
    else:
        print("Invalid Choice\n")
        continue_again()


    
