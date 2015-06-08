import bottle
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

app = bottle.default_app()

