#Creating Database

from sqlalchemy import create_engine,text

engine=create_engine("mysql+pymysql://root:2741@localhost:3307")

db_name="atm_machine"
def create_db():
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"The {db_name} is Created Sucessfully")

create_db()


