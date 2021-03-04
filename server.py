from flask import flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def happy_birthday():
    return "Happy birthday fucker"