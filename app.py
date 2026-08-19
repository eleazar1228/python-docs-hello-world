from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This is Eleazar! I love Jesus, and my wife Sydney!!This is the staging stage by the way!"
