import bottle
app = application = bottle.Bottle()

@app.route('/hello/<name>')
def index(name):
	return "Hello"
	#return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == '__main__':
	app.run()