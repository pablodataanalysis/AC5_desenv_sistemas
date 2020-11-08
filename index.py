from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/teste")
def inicial():
    return "Aula de Flask"

@app.route("/Flamengo")
def index():
    return render_template("Flamengo.html")

@app.route("/Fluminense")
def Fluminense():
    return render_template("Fluminense.html")

@app.route("/Botafogo")
def Botafogo():
    return render_template("Botafogo.html")

@app.route("/Vasco")
def Vasco():
    return render_template("Vasco.html")    

app.run()