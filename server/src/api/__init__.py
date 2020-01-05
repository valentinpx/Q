from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from random import randint

# Creating intance of Flask class: the application
app = Flask(__name__)

# Allowing api access from any server
CORS(app)

# Configuring database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../../db/qdb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Defining the db main table with a class
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

    def __init__(self, url):
        self.url = url
        self.upvotes = 0
        self.downvotes = 0

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
        return ({"id": id, "url": image.url, "votes": {"up": image.upvotes, "down": image.downvotes}})
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
        dest.insert(0, get_specified(image.id))
    return (jsonify(dest))

@app.route("/api/<id>/vote", methods = ['POST'])
def vote(id):
    image = Image.query.get(id)
    up = request.args.get('up')

    if (image != None):
        if (up == True):
            image.upvotes += 1
        else:
            image.downvotes += 1
        db.session.commit()
        return (get_specified(id))
    return ("Not found", 404)
