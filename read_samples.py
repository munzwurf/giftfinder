from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from db_setup import Questions, Answers, Products, Productattributes, Base

engine = create_engine('sqlite:///giftfinder.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

question_list = session.query(Questions).all()
print "Question List:"
for e in question_list:
	print e.name

answer_list = session.query(Answers).all()
print "Answer List:"
for e in answer_list:
	print e.name
	

product_list = session.query(Products).all()
print "Products List:"
for e in product_list:
	print e.name

productattributes_list = session.query(Productattributes).all()
print "Product Attribute List:"
for e in productattributes_list:
	print e.attribute

print "Filter Test:"
print session.query(Answers).filter_by(question_id = 2).first().name