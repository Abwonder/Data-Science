<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/hello1")
def hello_world1(): ## name of the function has to be unique hello_world1
    return "Hello, world!"


@app.route("/hello2")
def hello_world2():  ## name of the function has to be unique hello_world2
    return "Hello, world!"

if __name__=="__main__":
=======
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/hello1")
def hello_world1(): ## name of the function has to be unique hello_world1
    return "Hello, world!"


@app.route("/hello2")
def hello_world2():  ## name of the function has to be unique hello_world2
    return "Hello, world!"

if __name__=="__main__":
>>>>>>> 12fc83e62130cf8fd7b26f2cc1d7259d4bfbbd90
=======
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/hello1")
def hello_world1(): ## name of the function has to be unique hello_world1
    return "Hello, world!"


@app.route("/hello2")
def hello_world2():  ## name of the function has to be unique hello_world2
    return "Hello, world!"

if __name__=="__main__":
>>>>>>> 12fc83e62130cf8fd7b26f2cc1d7259d4bfbbd90
    app.run(host="0.0.0.0")