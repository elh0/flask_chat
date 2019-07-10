import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message us /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    return "Hi " + username

@app.route("/<username>/<message>")
def send_message(username, message):
return "{0}: {1}".format(username, message)

app.run(host='0.0.0.0', port=80, debug=True)