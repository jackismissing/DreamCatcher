from dreamcatcher import dreamcatcher

@dreamcatcher.route('/')
@dreamcatcher.route('/index')
def index():
	return "Hello World"
