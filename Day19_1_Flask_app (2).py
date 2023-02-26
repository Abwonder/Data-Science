from flask import Flask

# To be able to request input from the url import library request
from flask import request


app = Flask(__name__)   ## object of flask

@app.route("/")  ## decorate the function using @app.route - helps expose the function over the url to run dnan produce it
def hello_world():
    return "Hello, World!"

@app.route("/hello1")  ## decorate the function using @app.route - helps expose the function over the url to run dnan produce it
def hello_world1():
    return "Abwonder007 on api!"

@app.route("/hello2")  ## decorate the function using @app.route - helps expose the function over the url to run dnan produce it
def hello_world2():
    return "Another angle for ABwonder... API!"

## additional fuction
@app.route("/test_fun")
def test():
    a = 5+7
    return "This is my first fun in flask {}".format(a)
# https://red-fireman-xuonk.pwskills.app:5000/test_fun

## craating function that can accept request

@app.route("/input_url")
def request_input():
    data = request.args.get("x")
    return "This is my input url {}". format(data)
# https://red-fireman-xuonk.pwskills.app:5000/input_url?x=Abioye%20Oyatoye
# whatever we enter after input_url?x= will be the input that will be accepted and displayed or use for the operation
if __name__=="__main__":
    app.run(host="0.0.0.0")

## once run it changes it to server!!
## Note: I accessed this function on the url using
# https://red-fireman-xuonk.pwskills.app:5000 
# 5000 is the default