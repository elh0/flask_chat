import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello There</h1>"


"""
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
"""
app.run(host='0.0.0.0', port=80, debug=True)