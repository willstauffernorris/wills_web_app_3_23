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


#from web_app.routes.home_routes import home_routes
#from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    #app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)