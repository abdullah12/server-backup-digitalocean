you can read about python decorator


export FLASK_APP=main.py

to run then :
  flask run

# hello app
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
  
#static route
@app.route("/abdullah")
def hello():
    return "Hello abdullah!"

# dinamic route  
@app.route("/<string:name>")
def hello():
    name= name.capitilize()
    return f"Hello {name}!"
  
  