#1
from flask import Flask

app = Flask(__name__)

@app.route("/api/register/",  methods=['POST'])

def api():
    emilia = request.json
    correu = emilia['email']
    resultat = register_get_token(correu)
    return resultat+'\n'

#2
flask --app app run OR flask --app app run --debug

#3
Ctrl+C -> STOP
