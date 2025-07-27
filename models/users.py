from sqlalchemy import Column,String,Float,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from createdb import Base
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String(50))
    phone_num=Column(String(50))
    role=Column(String(50))
    
    place=Column(String(50))
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

    creater=relationship("User",remote_side=[id],foreign_keys=[created_by])
    modifier=relationship("User",remote_side=[id],foreign_keys=[modified_by])
    atm_created_by=relationship("Atm_machine",foreign_keys="Atm_machine.created_by",back_populates="atm_created_user")
    atm_modified_by=relationship("Atm_machine",foreign_keys="Atm_machine.modified_by",back_populates="atm_modified_user")
    

    account_created_by=relationship("Accountinfo",foreign_keys="Accountinfo.created_by",back_populates="account_created_user")
    account_modified_by=relationship("Accountinfo",foreign_keys="Accountinfo.modified_by",back_populates="account_modified_user")
    
    account_user=relationship("Accountinfo",foreign_keys="Accountinfo.user_id",back_populates="user")

   