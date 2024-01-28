from sqlalchemy import String, Integer, Column

from database import Base

class Ingreso(Base):
    __tablename__="tabla1"
    idregistro = Column(Integer, primary_key=True, index=True)
    carnet = Column(String(11))
    nombrepersona = Column(String(50))