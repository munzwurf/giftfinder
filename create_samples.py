
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
 
from db_setup import Questions, Answers, Products, Productattributes, Base

engine = create_engine('sqlite:///giftfinder.db', encoding = 'utf-8')
engine.raw_connection().connection.text_factory = str
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

question1 = Questions(name = "gender", sentence = "Fuer welches Geschlecht suchst du?")
question2 = Questions(name = "age", sentence = "Fuer welches Alter suchst du?")
question3 = Questions(name = "occasion", sentence = "Was ist der Anlass fuer den Geschenkekauf?")

gender = ['Maennlich','Weiblich']
age = ['0-10','11-20','21-30','31-40']
occasion = ['Geburtstag','Hochzeit','Advent','Jahrestag']

c=0
q = []
for x in gender:
	c=+1
	globals()['answer%s' % c] = Answers(name = x, question = question1)
	q.append(globals()['answer%s' % c])

for x in age:
	c=+1
	globals()['answer%s' % c] = Answers(name = x, question = question2)
	q.append(globals()['answer%s' % c])

for x in occasion:
	c=+1
	globals()['answer%s' % c] = Answers(name = x, question = question3)
	q.append(globals()['answer%s' % c])




p = []

for x in range(1, 9):
    globals()['product%s' % x] = Products(name = ('Gift{0}'.format(x)),price = "50")
for x in range(1,9):
	p.append(globals()['product%s' % x])

c = 0
pa = []
for x in range(1,9):
	c += 1
	globals()['pa%s' % c] = Productattributes(attribute = random.choice(gender), product = globals()['product%s' % x])
	p.append(globals()['pa%s' % c])
	c += 1
	globals()['pa%s' % c] = Productattributes(attribute = random.choice(age), product = globals()['product%s' % x])
	p.append(globals()['pa%s' % c])	
	c += 1
	globals()['pa%s' % c] = Productattributes(attribute = random.choice(occasion), product = globals()['product%s' % x])
	p.append(globals()['pa%s' % c])
	
	


session.add_all([question1,question2,question3])
session.add_all(q)
session.add_all(p)
session.add_all(pa)
session.commit()