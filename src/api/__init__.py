from flask import Flask

# Creating intance of Flask class, this will be the application
app = Flask(__name__)

# Defining what URL should trigger a function
@app.route("/")
def hello_world():
    return ("Hello World!")
