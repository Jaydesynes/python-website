from flask import Flask

app = Flask(__name__)


@app.route("/")
def Jaydesynes():
    return"<p>Welcome to Jaydesynes</p>"

@app.route("/About us")
def jaydesynes():
    return "<b>JAYDESYNES</b> is a Nigerian fast rising graphics company"

@app.route("/Contact us")
def jaydesynes():
    return "<b>JAYDESYNES</b> Contact us on Facebook, Instagram @Jaydesynes"

@app.route("/Our Services")
def jaydesynes():
    return "<b>JAYDESYNES</b> is a Nigerian fast rising graphics company"

@app.route("/About us")
def jaydesynes():
    return "<b>JAYDESYNES</b> is a Nigerian fast rising graphics company"
