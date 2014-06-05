from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/luca/alchimia/prova.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
# class Album(db.Model):
#     id = db.Column(db.String(10), primary_key=True)
#     Author = db.Column(db.String(80))
#     Title = db.Column(db.String(120))
#     Genre = db.Column(db.String(50))


#     def __init__(self, author, title, genre):
#         self.Author = author
#         self.Title = title
#         self.Genre = genre
#     def __repr__(self):
#         return '<Album %r>' % self.title

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