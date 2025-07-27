from models import accountinfo,atm_machine,users
from createdb import Base,engine1

Base.metadata.create_all(engine1)