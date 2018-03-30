"""
Flask is great for all kinds of web server projects.
See the docs here: http://flask.pocoo.org/docs/0.12/quickstart/
"""

from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

@app.route("/")
def index():
    return """<center>
        <h1>You have reached tbe Flask demo sever</h1>
        <small>I know this is a lazy solution...</small>
    </center>
    """

class FoodsAPI(MethodView):
    """
    MethodViews are a convenient way to make REST APIs in Flask
    See docs here: http://flask.pocoo.org/docs/0.12/api/#flask.views.MethodView
    """

    # Don't do this at home kids. Databases exist for a reason.
    foods = ["Steak", "Ribs", "Cherries"]

    def get(self):
        return jsonify(self.foods)

    def post(self):
        if not isinstance(request.json, dict):
            return "Invalid input. Expected JSON object.", 400
        else:
            newFood = request.json

            if "name" not in newFood:
                return "Invalid input. The food's name must be set.", 400
            else:
                self.foods.append(newFood["name"])
                return "Success"

app.add_url_rule("/api/foods", view_func=FoodsAPI.as_view("Foods"))

if __name__ == "__main__":
    app.run()