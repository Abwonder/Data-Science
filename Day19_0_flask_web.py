<<<<<<< HEAD

from flask import Flask   ### library flask imported
from flask import redirect


app = Flask(__name__)   ## building object of Flask

## firstly build individual function mapped to url
@app.route("/father")  
def father():
    return "Father's name is Olushola David"

@app.route("/mother")
def mother():
    return "Mothers's name is Felicia Asabi"

@app.route("/son")
def son():
    return "I am the son, my name is Abwonder"

## build the condition for using url_for
@app.route("/family/<name>") ## <name> denotes the sub for the condition
def family():  ## function for the condition for determination!!!!
    if name == "father":
        return redirect(url_for("father"))
    if name == "mother":
        return redirect(url_for("mother"))
    if name == "son":
        return redirect(url_for("son"))
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
 ### to check on your local host machine use:: http://127.0.0.1:5000/son
 #change the end point values to any of son, mother, father!!! 
=======

from flask import Flask   ### library flask imported
from flask import redirect


app = Flask(__name__)   ## building object of Flask

## firstly build individual function mapped to url
@app.route("/father")  
def father():
    return "Father's name is Olushola David"

@app.route("/mother")
def mother():
    return "Mothers's name is Felicia Asabi"

@app.route("/son")
def son():
    return "I am the son, my name is Abwonder"

## build the condition for using url_for
@app.route("/family/<name>") ## <name> denotes the sub for the condition
def family():  ## function for the condition for determination!!!!
    if name == "father":
        return redirect(url_for("father"))
    if name == "mother":
        return redirect(url_for("mother"))
    if name == "son":
        return redirect(url_for("son"))
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
 ### to check on your local host machine use:: http://127.0.0.1:5000/son
 #change the end point values to any of son, mother, father!!! 
 # 
 #  
>>>>>>> 12fc83e62130cf8fd7b26f2cc1d7259d4bfbbd90
