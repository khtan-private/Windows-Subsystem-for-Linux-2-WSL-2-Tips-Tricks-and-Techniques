import datetime
from platform import uname
from flask import Flask
app = Flask(__name__)

def getgreeting():
    return uname()[0] + " | " + uname()[1] + " | " + str(datetime.datetime.now())

@app.route("/")
def home():
    return f"<html><body><h1>{getgreeting()}</h1></body></html>"
