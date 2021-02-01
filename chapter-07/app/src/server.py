import datetime
from platform import uname
from flask import Flask
server = Flask(__name__)

@server.route("/")
def getgreeting():
    return uname()[0] + " | " + uname()[1] + " | " + str(datetime.datetime.now())

if __name__ == "__main__":
    server.run(host='0.0.0.0')
