from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/dodaj")
def new_pracownik():
    return render_template('pracownikadd.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
     if request.method == 'POST':
      try:
       imieinazwisko = request.form['imieinazwisko']
       nrpracownika = request.form['nrpracownika']
       adres = request.form['adres']
             
       with sql.connect("database.db") as con:
         cur = con.cursor()
         cur.execute("INSERT INTO pracownicy (nazwisko,nrpracownika,adres) VALUES (?,?,?)",(imieinazwisko,nrpracownika,adres) )

                    
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
