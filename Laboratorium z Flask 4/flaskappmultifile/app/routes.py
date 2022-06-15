from app import app

from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user
import sqlite3 as sql

app.config.update(DEBUG = True,SECRET_KEY = 'sekretny_klucz')

# ustawienie flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
 def __init__(self, id):
     self.id = id
     self.name = "uzytkownik" + str(id)
     self.password = self.name + "_secret"

 def __repr__(self):
     return "%d/%s/%s" % (self.id, self.name,self.password)
#generacja uzytkownikow
users = [User(id) for id in range(1, 10)]

@app.route("/")
@login_required
def main():
 return render_template('index.html')

@app.route("/formularz_logowania", methods=["GET", "POST"])
def login():
 tytul = 'Zaloguj się'
 if request.method == 'POST':
     username = request.form['username']
     password = request.form['password']
     if password == username + "_secret":
         id = username.split('user')[1]
         user = User(id)
         login_user(user)
         return redirect(url_for("main"))
     else:
         return abort(401)
 else:
       return render_template('formularz_logowania.html', tytul=tytul)


@app.errorhandler(401)
def page_not_found(e):
 tytul="Coś poszło nie tak..."
 blad = "401"
 return render_template('blad.html', tytul=tytul, blad=blad)

@app.route("/logout")
@login_required
def logout():
 logout_user()
 tytul="Wylogowanie"
 return render_template('logout.html', tytul=tytul)

@login_manager.user_loader
def load_user(userid):
 return User(userid)

@app.route("/about")
@login_required
def omnie():
 tytul = 'O mnie'
 return render_template('omnie.html', tytul=tytul)


@app.route("/dodaj")
@login_required
def new_student():
 return render_template('studentadd.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
 if request.method == 'POST':
     try:
      imieinazwisko = request.form['imieinazwisko']
      nrpracownika = request.form['nrpracownika']
      adres = request.form['adres']

      with sql.connect("database.db") as con:
          cur = con.cursor()
          cur.execute("INSERT INTO pracownicy (imieinazwisko,nrpracownika,adres) VALUES(?,?,?)",(imieinazwisko,nrpracownika,adres) )

          con.commit()
          msg = "Rekord zapisany"
     except:
         con.rollback()
         msg = "Blad przy dodawaniu rekordu"

     finally:
         return render_template("rezultat.html",msg = msg)
     con.close()
 
@app.route('/lista')
def list():
 con = sql.connect("database.db")
 con.row_factory = sql.Row
 cur = con.cursor()
 cur.execute('SELECT * FROM pracownicy ORDER BY imieinazwisko')
 rekordy = cur.fetchall();
 return render_template("lista.html",rekordy = rekordy)