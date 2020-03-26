
from flask import Blueprint
from sklearn.datasets import load_iris
from web_app.classifier import load_model

from sklearn.linear_model import LogisticRegression

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route('/stats/iris')
def iris():    
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)
    clf = load_model()
    return str(clf.predict(X[:2, :]))