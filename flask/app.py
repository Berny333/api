from flask import Flask, request, url_for, render_template
from db import register_get_token

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register/", methods=["GET"])
def show_form():
    return render_template("register.html")

@app.route("/gracies/", methods=["POST"])
def procesar():
    emilia = request.form.get("email")
    result = None
    result = register_get_token(emilia)
    if result != None:
        return render_template("gracies.html", emilia = emilia, token = result)
    else:
        return render_template("error.html", resposta = result)

@app.route("/api/register/",  methods=['POST'])

def api():
    emilia = request.json
    correu = emilia['email']
    resultat = register_get_token(correu)
    return resultat+'\n'



