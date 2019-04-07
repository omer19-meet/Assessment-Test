from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class applicant(Base):
    
    __tablename__ = 'applicants'

    id = Column(Integer, primary_key=True)
    national_id = Column(Integer)
    name = Column(String)
    age = Column(Integer)
    subject = Column(String)
