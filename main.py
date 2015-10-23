from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Questions, Answers, Products, Productattributes, Base
from wtforms import Form, BooleanField, TextField, PasswordField, validators, RadioField
import sqlalchemy

engine = create_engine('sqlite:///giftfinder.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

questions = session.query(Questions)
answers = session.query(Answers)
products = session.query(Products)


@app.route('/')
def Main():
	return render_template('main.html', questions = questions, answers = answers, products = products)
		

@app.route('/productlisting', methods=['GET','POST'])
def ProductListing():
		formvals = request.form
		l = ['Weiblich','Maennlich']
		gender = formvals.getlist('gender')[0]
		age = formvals.getlist('age')[0]
		occasion = formvals.getlist('occasion')[0]
		#prodattr = session.query(Productattributes).filter(Productattributes.attribute.in_([gender,age]))
		#prodattr = session.query(Productattributes).filter_by(attribute=gender)
		prodattr = session.query(Productattributes).filter(sqlalchemy.not_(Productattributes.attribute.in_([gender,age])))
		result = []
		print "Test"
		for i in prodattr:
			print i.product_id
			result.append(i.product_id)
		print result
		products = session.query(Products).filter(Products.id.in_(result))

		return render_template('productlisting.html', products = products)
		

@app.route('/questionnaire')
def Questionnaire():
	return render_template('questionform.html', questions = questions, answers = answers)
		
app.secret_key = 'secret'
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)