"""
Questo Modulo permette di gestire il magazzino,
si possono aggiungere, rimuore e modificare gli elementi del database.
Si basa su Flask e la sua estensione Flask-Admin.
"""
import os
import os.path as op
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from wtforms import validators
from flask import render_template
from flask.ext import admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import filters


# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = './records.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# Create models
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    genre = db.Column(db.Text)
    year = db.Column(db.Integer)
    thumbnail_url = db.Column(db.Text)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

class RecordAdmin(sqla.ModelView):
    view_excluded_columns = ['description', ]

# Create admin
admin = admin.Admin(app, 'Gestione Magazzino')

# Add views
admin.add_view(RecordAdmin(Record, db.session))

if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = op.realpath(os.path.dirname(__file__))
    database_path = op.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Start app
    app.run(port=6666, debug=True)