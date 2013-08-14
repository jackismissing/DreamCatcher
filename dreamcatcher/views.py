# -*- coding: utf-8 -*-
from dreamcatcher import dreamcatcher
from flask import render_template

@dreamcatcher.route('/')
@dreamcatcher.route('/index')
def index():
	user = { 'nickname': 'Nicolas' }
	return render_template("index.html", title="Home", user = user)

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
