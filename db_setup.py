import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Questions(Base):
	__tablename__ = 'questions'
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False)
	sentence = Column(String)
	description = Column(String)
	
class Answers(Base):
	__tablename__ = 'answers'
	id = Column(Integer, primary_key = True)
	question_id = Column(Integer, ForeignKey('questions.id'))
	question = relationship('Questions')
	name = Column(String, nullable = False)
	

class Products(Base):
	__tablename__ = 'products'
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False)
	description = Column(String)
	price = Column(String)
	imgpath = Column(String, default="gift.jpg")
	
class Productattributes(Base):
	__tablename__ = 'product_attributes'
	id = Column(Integer, primary_key = True)
	product_id = Column(Integer, ForeignKey('products.id'))
	attribute = Column(String)
	product = relationship('Products')

engine = create_engine('sqlite:///giftfinder.db')

Base.metadata.create_all(engine)
				