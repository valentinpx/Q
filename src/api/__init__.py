from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

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

# Defining what URL should trigger a function
@app.route("/")
def hello_world():
    return ("Q api version 1")

@app.route("/api/<id>")
def get_specified(id):
    image = Image.query.get(id)
    if (image != None):
        return (({"id": id, "url": image.url, "votes": {"up": image.upvotes, "down": image.downvotes}}))
    else:
        return ("Not found", 404)
