from os.path import exists
import json
import re
import secrets
from hashlib import pbkdf2_hmac

def dbopen(filename):
    #Condicional per mirar si el dbjson existeix
    if exists (filename):
        with open(filename) as fitxer:
            registres = json.load (fitxer)
    else :
        registres = {}
        registres['users'] = []
    # o registres = {'users': []}
    return registres


def savefile(registres, filename) :
    #guardar fitxer json
    with open(filename, 'w') as fitxer_modificat:
        json.dump(registres, fitxer_modificat, indent=4) 

#Retorna la posició de l'usuari si existeix o mostra un missatge de text si no
#y surt del programa.
#Pots fer servir el VALUE (token o email) que vulguis per buscar l'usuari
def exist_user(registres, value, target):
        for index, user in enumerate(registres.get("users")):
            if value == "token" :
                if user.get("token") == target:
                    return index
                else : 
                    print('El token no ha trobat cap coincidència')
            if value == "email" : 
                if user.get("email") == target:
                    return index
                else : 
                    print('El mail no ha trobat cap coincidència')
        exit(0)

def register_get_token(emilia):

    registres = dbopen("db.json")

    validate_email(emilia)

    #crear token
    token = secrets.token_urlsafe(32)

    #Afegir el nou registre la variable registres
    registres['users'].append({
    'email' : emilia,
    'token' : token
    })

    savefile(registres, "db.json")

    return token

def validate_email(emilia):
    if not re.match(r'[A-Za-z0-9]+[.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+', emilia):
        print("El correu electrònic no és vàlid")
        exit(0)
    return 'El correu electrònic és vàlid'
        
