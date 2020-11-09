from flask import Flask, render_template

app = Flask(__name__)

@app.route("/quartas")
def index():
    return render_template("index.html")

@app.route("/oitavas")
def oitavas():
    return render_template("oitavas.html")

@app.route("/palmeiras")
def palmeiras():
    return render_template("palmeiras.html")

@app.route("/flamengo")
def flamengo():
    return render_template("flamengo.html")

@app.route("/corinthians")
def corinthians():
    return render_template("corinthians.html")

@app.route("/vasco")
def vasco():
    return render_template("vasco.html")

@app.route("/saopaulo")
def saopaulo():
    return render_template("saopaulo.html")

@app.route("/fluminense")
def fluminense():
    return render_template("fluminense.html")

@app.route("/santos")
def santos():
    return render_template("santos.html")

@app.route("/botafogo")
def botafogo():
    return render_template("botafogo.html")

app.run(debug=True)
