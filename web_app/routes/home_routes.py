from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    print('visted the HOME page')
    return render_template("prepare_to_predict.html")



@home_routes.route("/hello")
def hello():
    x = 2 + 2
    print('visted hello page')
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print('visted about page')
    return "About me"


@home_routes.route("/river")
def river():
    print('visted rivers page')
    return "A page about my favorite rivers"