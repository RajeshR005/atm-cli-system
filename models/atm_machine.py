from sqlalchemy import Column,String,Float,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from createdb import Base
from datetime import datetime

class Atm_machine(Base):
    __tablename__="atm_machine"
    id=Column(Integer,autoincrement=True,primary_key=True)
   
    Amount=Column(Integer)
    no_of_fivehundred=Column(Integer)
    no_of_hundred=Column(Integer)
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

    atm_created_user=relationship("User",foreign_keys=[created_by],back_populates="atm_created_by")
    atm_modified_user=relationship("User",foreign_keys=[modified_by],back_populates="atm_modified_by")
