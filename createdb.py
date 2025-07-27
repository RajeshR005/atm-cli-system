#Creating Database

from sqlalchemy import create_engine,text
from sqlalchemy.orm import declarative_base,sessionmaker

Base=declarative_base()
engine=create_engine("mysql+pymysql://root:2741@localhost:3307")
engine1=create_engine("mysql+pymysql://root:2741@localhost:3307/atm_machine")

db_name="atm_machine"
def create_db():
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"The {db_name} is Created Sucessfully")

# create_db()


Session=sessionmaker(engine1)
db=Session()