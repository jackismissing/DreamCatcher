# -*- coding: utf-8 -*-
from dreamcatcher import dreamcatcher, lm
from models import User
from forms import LoginForm, SignupForm
from flask import render_template, flash, redirect, request, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required


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
Flask-login load_user method
'''
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))


'''
Flask-login before request method
'''
@dreamcatcher.before_request
def before_request():
	g.user = current_user


'''
Signing route 
'''
@dreamcatcher.route('/signin', methods = ['GET', 'POST'])
def signin():

	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))

	form = LoginForm()

	if request.method == 'POST':	
		user = form.validate_user()

		if user is not False:
			login_user(user)
			flash('User successfuly singed in')
			return redirect(url_for('index'))

	else:
		return render_template('login.html', form = form)

	
'''
Signing out route
'''
@dreamcatcher.route('/signout')
def signout():
	logout_user()
	return redirect(url_for('index'))


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
			if register_user is not None:
				login_user(register_user)
				flash('User succesfuly registered')
				return redirect(url_for('index'))

	elif request.method == 'GET':
		return render_template('signup.html', form = form)


'''
User page route
'''
@dreamcatcher.route('/user/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username = username).first()
	if user is None:
		flash('User ' + username + ' not found')
		return redirect(url_for('index'))

	dreams = [
		{ 'title': 'Dream title', 'content': 'Bacon ipsum dolor sit amet drumstick brisket cow pork chop short loin pork loin tenderloin venison hamburger. Fatback capicola swine, ribeye pastrami tail jerky brisket kielbasa boudin. Strip steak sirloin ground round shank beef ribs hamburger tenderloin. Bacon turkey flank, pancetta ground round tail chicken frankfurter venison. Strip steak sirloin leberkas pastrami salami shank prosciutto kielbasa. Jerky shoulder pork bresaola. T-bone cow jerky venison, biltong meatloaf prosciutto brisket jowl ribeye tri-tip tongue capicola shoulder.'},
		{ 'title': 'Dream title', 'content': 'Bacon ipsum dolor sit amet drumstick brisket cow pork chop short loin pork loin tenderloin venison hamburger. Fatback capicola swine, ribeye pastrami tail jerky brisket kielbasa boudin. Strip steak sirloin ground round shank beef ribs hamburger tenderloin. Bacon turkey flank, pancetta ground round tail chicken frankfurter venison. Strip steak sirloin leberkas pastrami salami shank prosciutto kielbasa. Jerky shoulder pork bresaola. T-bone cow jerky venison, biltong meatloaf prosciutto brisket jowl ribeye tri-tip tongue capicola shoulder.'}
	]

	return render_template('user.html', user = user, dreams = dreams)


