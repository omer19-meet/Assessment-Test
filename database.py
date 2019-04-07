from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_applicant(national_id , name, age, subject):
	applicant_1 = applicant(national_id=national_id, name=name, age=age, subject=subject)
	session.add(applicant_1)
	session.commit()

def get_appilcants():
	applicantss = session.query(applicant).all()
	return applicantss