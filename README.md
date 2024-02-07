#1

pip install flask 

#2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#3
flask --app hello run OR flask --app hello run --debug

#4
Ctrl+C -> STOP