from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prova.db'
db = SQLAlchemy(app)

class Album(db.Model):
    id = db.Column(db.String, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    
    def __init__(self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre

    def __repr__(self):
        return 'Album {}'.format(self.title)

@app.route('/hello')
def hello():
	string = ""
	user = User.query.all()
	for i in user:
		string += "<p>" + i.email + " "
		string += i.username + "</p>"
	return string
@app.route('/ciao')
def ciao():
	return "ciao mondo"

if __name__ == '__main__':
	# db.create_all()
	# admin = User('adminaa', 'adminaa@example.com')
	# guest = User('guestaa', 'guestaa@example.com')
	# # # maligno = Album('Capro', 'Maligno','Sludge')
	# # # badthings = Album('Carcione', 'Bad Things','Blues')
	# db.session.flush()
	# db.session.add(admin)
	# db.session.add(guest)
	# db.session.commit()
	#debug andra tolto
	app.debug = True
	#il tutto viene avviato qui: http://localhost:porta/
	app.run(port = 5000)