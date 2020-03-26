
import os
from dotenv import load_dotenv

from flask import Flask

#app = Flask(__name__)

from web_app.models import db, migrate
from web_app.routes.admin_routes import admin_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.user_routes import user_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.stats_routes import stats_routes

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', default = "super secret") # todo: pass from env var (enables flash messaging)
DATABASE_URL = os.getenv("DATABASE_URL", default= "sqlite:///wills_web_app_3_23.db")

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wills_web_app_3_23.db"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/mjr/Desktop/web-app-inclass-11/web_app_12.db"

    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(admin_routes)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(stats_routes)


    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)