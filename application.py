import requests
import flask.sessions
import flask
import mysql.connector

from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash



con = mysql.connector.connect()
db = SQL("http//:localhost/decaflix")

@app.route('/login')
def login():
   username = requests.form.get("username")
   password = requests.form.get("password")
   hashed  = generate_password_hash(password)
   res = db.execute("select * from databas where username = :username", username)
   if res[0]['hash'] == hash:
      session['id'] == res[0]['user_id']
      return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
   pass

@app.route('/', methods=['GET', 'POST'])
def method_name():
   pass