from createdb import db
from models import *
from utility import *


def account_holder_deposit(card_no):
    pin_no=input("Enter your PIN: ")
    user=check_auth(card_no.atm_card_no,pin_no)
    if isinstance(user,str):
            print (user)
            continue_again_user(card_no)

    Add_cash(user)

def check_balance_holder(card_no):
      user_pin=check_pin(card_no)
      if not user_pin:
            print("Invalid PIN")
            continue_again_user(card_no)
      print(f"Available Balance: {card_no.avail_balance}")
      continue_again_user(card_no)

def withdrawl_amount(card_no):
      user_pin=check_pin(card_no)
      if not user_pin:
            print("Invalid PIN")
            continue_again_user(card_no)
      print("If you want : \
            \n₹500 = 1\
            \n₹100 = 2\
            \n(or) Enter your prefered Amount = 3")
      while True:
        prefer_choice=int(input("Enter Your choice: "))
        if prefer_choice in [1,2]:
             break
        if prefer_choice >=100 and prefer_choice%100==0:
             break
        else:
             print("Enter Valid Amount !")  
      atm_debit(prefer_choice,card_no) 

def change_pin(card_no):
     user_pin=check_pin(card_no)
     if not user_pin:
          print("Invalid PIN")
          continue_again_user(card_no)
     while True:
        new_pin=input("Enter your New four Digit PIN")
        if len(new_pin)==4:
             card_no.pin_no=hash_pin(new_pin)
             db.commit()
             print("New PIN set successfully")
             continue_again_user(card_no)
        else:
             print("Enter a Valid Four Digit PIN")
                
     
    

