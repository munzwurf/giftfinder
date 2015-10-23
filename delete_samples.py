from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from db_setup import Questions, Answers, Products, Productattributes, Base

engine = create_engine('sqlite:///giftfinder.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

session.query(Questions).delete()
session.query(Answers).delete()
session.query(Products).delete()
session.query(Productattributes).delete()

session.commit()
print "All Samples deleted"