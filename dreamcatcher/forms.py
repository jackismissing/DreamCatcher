from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import Required, Email
from models import User, db


class LoginForm(Form):

	email = TextField('email', validators = [Required(), Email()])
	password = PasswordField('password', validators = [Required()])
	submit = SubmitField('Login to your account')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	'''
	Form & Email & Password validation
	'''
	def validate_user(self):
		if not Form.validate(self):
			return False

		user = User.query.filter_by(email = self.email.data).first()
		if user and user.check_password(self.password.data):
			return user
		else:
			self.email.errors.append('Invalid email or password')
			return False


class SignupForm(Form):

	username = TextField('username', validators = [Required()])
	email = TextField('email', validators = [Required(), Email()])
	password = PasswordField('password', validators = [Required()])
	submit = SubmitField('Create account')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	'''
	Form & Email validation
	'''
	def validate(self):
		if not Form.validate(self):
			return False

		user = User.query.filter_by(email = self.email.data).first()
		
		if user:
			self.email.errors.append('Email already taken')
			return False
		else:
			return True

	'''
	User registration : saving user to db and signing to the app with session
	'''
	def register_user(self, username, email, password):
		try:
			newuser = User(username = username, email = email, password = password)
			db.session.add(newuser)
			db.session.commit()
			user = User.query.filter_by(email = email).first()
			return user
		except Exception as e:
			db.session.flush()
			return None
