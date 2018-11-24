from flask import Flask,redirect,url_for

app = Flask(__name__)

def hello(): #program does nothing as written
   return 'hello world'

@app.route('/')
def index():
  return hello()

@app.route('/aboutus')
def about():
  return 'about us more'

# name is a string varible
@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello %s' %name

# postid is integer you can not put string in the url
@app.route('/hello/<int:postid>')
def post_show(postid):
  return 'I am post number: %d' %postid



# url_for()
@app.route('/users/<user>')
def explain_urlfor(user):
  if user == 'admin':
    return redirect(url_for('hello_name', name = user))
  else:
    return redirect(url_for('about'))
  

if __name__ == "__main__":
  app.run(port=8081,host='0.0.0.0', debug=True)
  
