from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")#parte do Luiz
def index():
    return render_template("index.html")

@app.route("/oitavas")
def index():
    return render_template("oitavas.html")

@app.route("/palmeiras")
def index():
    return render_template("palmeiras.html")

@app.route("/flamengo")
def index():
    return render_template("flamengo.html")

@app.route("/corinthians")
def index():
    return render_template("corinthians.html")

@app.route("/vasco")
def index():
    return render_template("vasco.html")

@app.route("/saopaulo")
def index():
    return render_template("saopaulo.html")

@app.route("/fluminense")
def index():
    return render_template("fluminense.html")

@app.route("/santos")
def index():
    return render_template("santos.html")

@app.route("/botafogo")
def index():
    return render_template("botafogo.html")

app.run(debug=True)