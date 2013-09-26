# -*- coding: utf-8 -*-
from dreamcatcher import dreamcatcher
from users import Profile
from forms import LoginForm, SignupForm
from flask import session, render_template, flash, redirect, request, url_for


'''
Index route
'''
@dreamcatcher.route('/')
@dreamcatcher.route('/index')
def index():
	user = { 'nickname': 'Nicolas' }
	return render_template("index.html", title="Home", user = user)


'''
Dreams/Posts route
'''
@dreamcatcher.route('/dreams')
def showDreams():
	begin = 'Last night, I dreamed that'
	dreams = [
		{
			'author' : { 'nickname': 'Jackismissing' },
			'content' : '%s I was coding' % begin
		},
		{
			'author' : { 'nickname': u'Chloé' },
			'content' : '%s I was flying with a duck' % begin
		}
	]

	return render_template("dreams.html", title = "Dreams", dreams = dreams)


'''
Login route 
'''
@dreamcatcher.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	
	if request.method == 'POST':
		if form.validate() == False:
			return render_template('login.html', form = form)
		else:
			login = form.login(form.email.data)
			return redirect(url_for('profile')) if login else 'not okay'
	elif request.method == 'GET':
		return render_template('login.html', form = form)


'''
Signup route
'''
@dreamcatcher.route('/signup', methods = ['GET', 'POST'])
def signup():
	form = SignupForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form = form)
		else:
			register_user = form.register_user(form.username.data, form.email.data, form.password.data)

			return redirect(url_for('profile')) if register_user else 'not okay'


	elif request.method == 'GET':
		return render_template('signup.html', form = form)

'''
Profile route
'''
@dreamcatcher.route('/profile')
def profile():

	if 'email' not in session:
		#return redirect(url_for('signin'))
		return 'no email in session'

	profile = Profile()
	user = profile.get_user(session['email'])

	if user is None:
		#return redirect(url_for('signin'))
		return 'no user'
	else:
		return render_template('profile.html', username = user.username)





