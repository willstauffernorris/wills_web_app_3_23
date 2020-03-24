from flask import Blueprint, render_template, jsonify

from web_app.services.twitter_service import ____
twitter_routes = Blueprint('twitter_routes', __name__)

@twitter_routes.route('/users/<screen_name>')
def get_user(screen_name=None):
    print(screen_name)
    return screen_name