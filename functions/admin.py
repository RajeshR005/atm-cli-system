import random
from createdb import db
from models import *
from utility import user_details,hash_pin,continue_again

def add_account_users(admin_id):
    name=input("Enter the Name of Account Holder: ")
    while True:
        phone_num=input("Enter the Phone Number")
        if len(phone_num)==10:
            break
        else:
            print("Invalid Phone Number")
    role="Account_holder"
    place=input("Enter the Native: ")
    Account_no=str(random.randint(10**9, 10**10 - 1))
    atm_card_no=(str(random.randint(10**9, 10**10 - 1)))
    pin_no=hash_pin('1234')
    avail_balance=int(input("Enter the First Deposit: "))
    created_by=admin_id
    modified_by=admin_id
    check_exist_user=db.query(User).filter(User.phone_num==phone_num).first()
    if check_exist_user:
        print("User Details Already Exists")
        continue_again()
    new_user=User(name=name,phone_num=phone_num,role=role,place=place,created_by=created_by,modified_by=modified_by)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    new_account=Accountinfo(user_id=new_user.id,Account_no=Account_no,atm_card_no=atm_card_no,avail_balance=avail_balance,pin_no=pin_no,created_by=created_by,modified_by=modified_by)
    
    db.add(new_account)
    db.commit()

    user_data=user_details(new_user.id)
    print(user_data)

    continue_again()

def change_user_account_in_active():
    account_number=input("Enter Account Number: ")
    change_status=db.query(Accountinfo).filter(Accountinfo.status==1,Accountinfo.Account_no==account_number).first()
    if not change_status:
        print("No User Data found")
        continue_again()
    change_status.status=0
    db.commit()
    print("Account De-Activated Sucessfully")

def change_user_account_active():
    account_number=input("Enter Account Number: ")
    change_status=db.query(Accountinfo).filter(Accountinfo.status==0,Accountinfo.Account_no==account_number).first()
    if not change_status:
        print("No User Data found")
        continue_again()
    change_status.status=1
    db.commit()
    print("Account Re-Activated Sucessfully")

    
    

    



    