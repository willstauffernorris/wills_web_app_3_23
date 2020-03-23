from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x = 2 + 2
    print('visted hello page')
    return f"Hello World! {x}"

@app.route("/about")
def about():
    print('visted about page')
    return "About me"


@app.route("/river")
def river():
    print('visted rivers page')
    return "A page about my favorite rivers"
