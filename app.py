from flask import Flask, request, url_for, render_template
from db import register_get_token

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register/", methods=["GET"])
def show_form():
    return render_template("register.html")

@app.route("/gracies/", methods=["POST"])
def procesar():
    emilia = request.form.get("email")
    result = register_get_token(emilia)
    if result == 'Correu registrat correctament':
        return render_template("gracies.html", resposta = emilia)
    else:
        return render_template("error.html", resposta = result)

@app.route("/api/register/",  methods=['POST'])

def api():
    emilia = request.json
    correu = emilia['email']
    resultat = register_get_token(correu)
    return resultat+'\n'



