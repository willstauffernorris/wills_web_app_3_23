from flask import Flask

#app = Flask(__name__)

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wills_web_app_3_23.db"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/mjr/Desktop/web-app-inclass-11/web_app_12.db"

    db.init_app(app)
    migrate.init_app(app, db)



    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)


    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)