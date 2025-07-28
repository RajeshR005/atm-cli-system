# 🏧 ATM CLI System

![Banner](https://capsule-render.vercel.app/api?type=waving&color=18b4f8&height=200&text=ATM%20CLI%20Banking%20System&fontAlignY=35&fontSize=40&desc=Secure%20Command-Line%20Banking%20Application&descSize=20)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-orange?style=for-the-badge&logo=sqlalchemy" />
  <img src="https://img.shields.io/badge/CLI%20App-Terminal-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" />
</p>

---

## 🎯 Project Overview

This is a **realistic simulation of an ATM Banking System** built as a command-line interface using Python and SQLAlchemy. It mimics how a real ATM and banking backend works:

✅ Role-based login for Admin & Account Holders  
✅ PIN-authenticated transactions with secure hashing  
✅ Real-time ATM cash management (₹500, ₹100 notes)  
✅ Balance checking, deposits, and smart withdrawals  
✅ Complete DB design using SQLAlchemy ORM

> ⚡ This project is modular, robust, and can scale into a GUI/REST-based version in the future.

---

## 🏗️ Folder Structure

```bash
ATM - Machine/
├── createdb.py                  # DB session setup
├── create_table.py              # Creates all tables
├── main.py                      # App entry point
├── menu_atm.py                  # Menu routing logic
├── utility.py                   # Helper functions (PIN check, hashing, continue logic)
├── functions/
│   ├── admin.py                 # Admin-specific actions
│   └── account_holder.py        # Holder-specific actions
├── models/
│   └── __init__.py              # SQLAlchemy models (User, Accountinfo, ATM)
```

---

## 🔐 Roles & Authentication

| Role           | Auth Type      | Description                |
|----------------|----------------|----------------------------|
| `Admin`        | Admin ID + PIN | Manages accounts, ATM cash |
| `Account Holder` | Card No + PIN | Deposit, Withdraw, Balance |

### 🔐 Password Security:
All user PINs are hashed using **bcrypt** via `passlib` before storing in the DB.

---

## ⚙️ Features Covered

### ✅ Admin Functionalities:
- Add new Account Holders (auto ATM and Account no)
- Activate / Deactivate accounts
- Load cash into ATM (`₹500` and `₹100` notes separately)
- Check ATM cash status

### ✅ Account Holder Functionalities:
- Secure login with PIN
- Check balance
- Deposit cash (updates user balance)
- Withdraw cash (dispenses lowest no of notes)
- Change PIN
- Smart role-based menu flow (no recursive call)

---

## 🧠 Core Logic Highlights

### 🔄 Withdrawal Logic:
Dispenses minimum number of notes based on ATM's available ₹500 and ₹100 notes.

```python
for count_500 in range(min(amount // 500, available_500), -1, -1):
    remaining = amount - (count_500 * 500)
    if remaining % 100 == 0:
        count_100 = remaining // 100
        if count_100 <= available_100:
            ...
```

✅ Avoids invalid cash combinations  
✅ Reverts gracefully if ATM doesn’t have proper note splits

### 🔁 Smart Menu Flow:
- After each operation, user/admin is prompted:
  ```
  Visit Menu = 1
  Exit       = 2
  ```
- No recursion: clean role-based redirection
- Admin sees only admin menu, user sees only holder menu

---

## 🧪 Sample Flow

1. Run `create_table.py` to set up DB
2. Start app with `main.py`
3. Admin login → Load ATM → Add users
4. Account Holder login → Deposit → Withdraw → Balance
5. Admin can deactivate/reactivate users
6. System reflects changes immediately

---

## 🐍 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/RajeshR005/atm-cli-system.git
cd ATM\ -\ Machine/

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install packages
pip install -r requirements.txt

# Create tables
python create_table.py

# Start CLI ATM
python main.py
```

---

## 🔍 Edge Cases Handled

- 🔐 Invalid PIN or Card Number
- 🏧 Insufficient ATM cash
- 🧾 Invalid denominations (non ₹100 multiples)
- 💰 Insufficient user balance
- 👥 Duplicate phone number check while creating user
- 🔄 Menu redirection is role-specific
- 💾 ATM and User balances update dynamically

---

## 🛠️ Tech Stack

| Tech              | Usage                         |
|------------------|-------------------------------|
| 🐍 Python 3.10+    | Core CLI Logic                |
| 🛢️ SQLAlchemy      | ORM for DB Models             |
| 🔐 Passlib (bcrypt)| PIN Hashing                  |
| 💽 MySQL          |  Backend DB        |
| 🧪 CLI Input       | Terminal-based user interface |


## 🤝 Contribution

```bash
# Fork the repo
# Create a branch for your feature
git checkout -b fix/feature-name

# Make changes & commit
git commit -m "Added: feature description"

# Push and PR
git push origin fix/feature-name
```

Pull Requests are welcome 🚀

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it with credits.

---

## 👨‍💻 Author

Made with ❤️ by [Rajesh R](https://www.linkedin.com/in/rajeshradha)  
🔗 GitHub: [RajeshR005](https://github.com/RajeshR005)

> 💬 “Building real-world logic that banks can trust — even in CLI!”
