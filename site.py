import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk
from flask import render_template
app = Flask(__name__)
table = [
    {
        "NUMERO\n": [
            "1",
            "2",
            "3",
            "4"
        ]
    },
    {
        "NOME": [
            "MARIA ",
            "JOAO",
            "CAROL",
            "CARLA"

        ]
    },
    {
        "IDADE": [
            "20",
            "19",
            "22",
            "18"

        ]
    },
    {
        "CIDADE": [
            "CAMACARI",
            "MACEIO",
            "GERMANY",
            "BROOKLYN"

        ]
    },
    {
        "PAÍS": [
            "BRASIL",
            "BRASIL",
            "ALEMANHA",
            "EUA"
        ]
    },

]
nome = "Ana Laura"
@app.route("/")
def homepage():
    return   render_template("homepage.html",table = table,nome=nome)

if __name__ == "__main__":
    app.run(debug=True)
