from utility import check_auth
from functions.admin import *
print(" Welcome to Prince Banking Services ")
print("------------------------------------")
def menus():
    print("The Options are: \
    \nAdmin = 1\
    \nAccount Holder = 2")
    Enter_choice=int(input("\nEnter your Choice: "))
    if Enter_choice==1:
        admin_id=input("\nEnter your Admin ID: ")
        pin=input("Enter your PIN: ")
        check_admin=check_auth(admin_id,pin)
        if isinstance(check_admin,str):
            print (check_admin)
            exit()
        if not check_admin.role=="admin":
            print("You are not Authorized Here !")
        print("\nAdmin Login Successful")
        print("\nThe Options are: \
              \nAdd Account Users = 1 \
              \nDe-activate Account users =2 \
              \nActivate Account users =3 \
              \nCheck Available Balance In ATM = 4\
              \nAdd Cash In ATM = 5 \
              \nCheck Past Transactions = 6\
              \nExit = 7")
        # print(f"{check_admin.id}{check_admin.name}")
        admin_choice=int(input("\nEnter your choice: "))
        if admin_choice==1:
            add_account_users(check_admin.id)
        elif admin_choice==2:
            change_user_account_in_active()
        elif admin_choice==3:
            change_user_account_active()
            



# menus()


