from dreamcatcher import db
from flaskext.bcrypt import generate_password_hash, check_password_hash

'''
User Model
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(12))
    dreams = db.relationship('Dream', backref = 'dreamer', lazy = 'dynamic')

    '''
    Init function, hashes user password
    '''
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    '''
    Flask login 
    '''
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    '''
    Model name representation
    '''
    def __repr__(self):
        return '<User %r>' % (self.username)

    '''
    Hashes passwords
    '''
    def set_password(self, passwordpost):
        self.password = generate_password_hash(passwordpost, 10)

    '''
    Checks hashed passwords
    '''
    def check_password(self, passwordpost):
        return check_password_hash(self.password, passwordpost)

'''
Dream Model
'''
class Dream(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(55))
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Dream %r>' % (self.body)

