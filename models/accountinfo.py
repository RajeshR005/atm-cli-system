from sqlalchemy import Column, Numeric,String,Float,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from createdb import Base
from datetime import datetime

class Accountinfo(Base):
    __tablename__="Accountinfos"
    id=Column(Integer,autoincrement=True,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    Account_no=Column(String(50))
    

    atm_card_no=Column(String(50))
    pin_no=Column(String(500))
    avail_balance = Column(Numeric(10, 2))
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

    account_created_user=relationship("User",foreign_keys=[created_by],back_populates="account_created_by")
    account_modified_user=relationship("User",foreign_keys=[modified_by],back_populates="account_modified_by")

    user=relationship("User",foreign_keys=[user_id],back_populates="account_user")