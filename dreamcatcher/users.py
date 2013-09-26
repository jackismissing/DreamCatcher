from models import User

class Profile():

	def get_user(self, email):
		user = User.query.filter_by(email = email).first()
		return user
