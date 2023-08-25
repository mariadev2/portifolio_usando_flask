from flask import Flask
from flask import render_template

app = Flask(__name__)
table = {
        "number": 1,
        "nome": "Maria Eduarda",
        "age": 20,
        "city": "Camaçari",
        "Country": "Brasil"
}
@app.route("/")
def homepage():
    return   render_template("homepage.html",table = table)

if __name__ == "__main__":
    app.run(debug=True)
