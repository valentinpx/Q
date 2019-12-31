from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from random import randint

# Creating intance of Flask class: the application
app = Flask(__name__)

# Configuring database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../../db/qdb.db"
db = SQLAlchemy(app)

# Defining the db main table with a class
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

# Function(s) needed to sort
def popularity(image):
    return (image.upvotes - image.downvotes)

def random_int(image):
    return (randint(0, 100))

# Defining what URL should trigger a function
@app.route("/")
def hello_world():
    return ("Q api version 0")

@app.route("/api/<id>")
def get_specified(id):
    image = Image.query.get(id)

    if (image != None):
        return (({"id": id, "url": image.url, "votes": {"up": image.upvotes, "down": image.downvotes}}))
    else:
        return ("Not found", 404)
@app.route("/api/random-q")
def get_random():
    images = Image.query.all()

    images.sort(key=random_int)
    return (get_specified(images[0].id))

@app.route("/api")
def list_all():
    images = Image.query.all()
    dest = []

    images.sort(key=popularity)
    for image in images:
        dest.append(get_specified(image.id))
    return (jsonify(dest))
