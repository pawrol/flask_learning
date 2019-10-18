# -*- coding: utf-8 -*-
# quiz/quiz.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

QUESTIONS = [
	{
		'question': u'Który film zdobył Oscara w 2016 roku w kategorii "najlepszy film"?',
		'answers': [u'Zjawa', u'Pan Tadeusz', u'Gladiator'],
		'correct_answer': u'Zjawa', 
	},
	{
		'question': u'Kultowa już postać gangstera "Siary" z "Kilera" miała w filmie na imię:', 
		'answers': [u'Waldek', u'Stefan', u'Jurek'], 
		'correct_answer': u'Stefan',
	},
	{
		'question': u"Ulubione zabawki Andy'ego z 'Toy Story', Chudy i Buzz, to:", 
		'answers': [u'Konwboj i astronauta', u'Klocki LEGO', u'Kapitan Ameryka i Ken'], 
		'correct_answer': u'Konwboj i astronauta', 
	},
 	{
		'question': u"W którym filmie Alfreda Hitchocka oglądaliśmy słynną scenę rozgrywającą się pod prysznicem?", 
		'answers': [u'Ptaki', u'Psychoza', u'Lśnienie'], 
		'correct_answer': u'Psychoza', 
 }
]
@app.route('/')
def index():
 return render_template('index.html', questions=QUESTIONS)
if __name__ == '__main__':
	app.run(debug=True)
