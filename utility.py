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

def continue_again_user(card_no):
    print("\nIf you want to \
          \nVisit  Menu's = 1\
          \nExit = 2")
    user_choice=int(input("\nEnter Your choice: "))
    if user_choice==1:
        from menu_atm import account_holder_menu
        account_holder_menu(card_no)
    elif user_choice==2:
        exit()
    else:
        print("Invalid Choice\n")
        continue_again_user(card_no)

def continue_again_admin(card_no):
    print("\nIf you want to \
          \nVisit  Menu's = 1\
          \nExit = 2")
    user_choice=int(input("\nEnter Your choice: "))
    if user_choice==1:
        from menu_atm import admin_menu
        admin_menu(card_no)
    elif user_choice==2:
        exit()
    else:
        print("Invalid Choice\n")
        continue_again_admin(card_no)



    
#----------------------------------------------------------------------------

#Add cash in ATM

def Add_cash(user):
    deposit=db.query(Atm_machine).filter(Atm_machine.status==1).first()
    fives=int(input("Enter No of ₹500 Notes: "))
    hundreds=int(input("Enter No of ₹100 Notes: "))
    user_deposit=fives*500+hundreds*100
    deposit.Amount=deposit.Amount+user_deposit
    deposit.no_of_fivehundred=deposit.no_of_fivehundred+fives
    deposit.no_of_hundred=deposit.no_of_hundred+hundreds

    print(f"Deposit Amount Summary\
          \n₹500 Notes: {fives}\
          \n₹100 Notes: {hundreds}\
          \nTotal Deposit Amount: {user_deposit}")
    confirmation=int(input("Confirm Deposit\
                           \nYes = 1\
                           \nNo = 2\
                           \nEnter Your choice: "))
    if confirmation==1:
        if user.role=="admin":
            db.commit()
            print(f"Cash Deposited Successfully\
                  \nDeposited Amount: {user_deposit}\
                  \nTotal Amount in ATM: {deposit.Amount}")
            continue_again_admin(user)
            
        else:
            
            account=db.query(Accountinfo).filter(Accountinfo.user_id==user.id,Accountinfo.status==1).first()
            account.avail_balance=account.avail_balance+user_deposit
            db.commit()
            print(f"Available Balance: {account.avail_balance}")
            continue_again_user(account)
                


#----------------------------------------------------------------------------------------------------------------------------

#check Pin
def check_pin(card_no):
    pin_no=input("Enter your PIN: ")
    check_pin=verify_pin(pin_no,card_no.pin_no)
    return check_pin
       
        
#----------------------------------------------------------------------------------------

#Cash withdrawl

def atm_debit(choice,card_no):
    if choice == 1:
        amount=500
    if choice == 2:
        amount = 100
    else:
        amount=choice
    user_account=db.query(Accountinfo).filter(Accountinfo.atm_card_no==card_no.atm_card_no).first()
    if amount>user_account.avail_balance:
        print("In Sufficient Balance in Your Account")
        continue_again_user(card_no)

    atm=db.query(Atm_machine).filter(Atm_machine.status==1).first()
    if amount>atm.Amount:
        print("In Sufficient Balance in ATM")
        continue_again_user(card_no)
    available_500=atm.no_of_fivehundred
    available_100=atm.no_of_hundred
    flag=False
    five_hundred=0
    hundred=0
    for count_500 in range(min(amount // 500, available_500), -1, -1):
        remaining = amount - (count_500 * 500)
        if remaining % 100 == 0:
            count_100 = remaining // 100
            if count_100 <= available_100:
                five_hundred=count_500
                hundred=count_100
                flag=True
                break
    if not flag:
        print("Cannot Dispense Amount with Available notes")
        continue_again_user(card_no)
    debit_amount=five_hundred*500+hundred*100
    atm.no_of_fivehundred=atm.no_of_fivehundred-five_hundred
    atm.no_of_hundred=atm.no_of_hundred-hundred
    atm.Amount=atm.Amount-debit_amount
    user_account.avail_balance=user_account.avail_balance-debit_amount

    print(f"Collect Your Cash: ₹500 notes {five_hundred} and ₹100 notes {hundred} ")
    db.commit()
    continue_again_user(card_no)

    



