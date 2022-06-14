import sqlite3

conn = sqlite3.connect('database.db')
print("BD otwarta")

conn.execute('CREATE TABLE pracownicy (imieinazwisko TEXT, nrpracownika TEXT,adres TEXT)')
print("Tabela utworzona")

cur = conn.cursor()
cur.execute("INSERT INTO pracownicy (imieinazwisko,nrpracownika,adres) VALUES(?,?,?)",('Pazura','2','Polna 2') )
cur.execute("INSERT INTO pracownicy (imieinazwisko,nrpracownika,adres) VALUES(?,?,?)",('Antkiewicz','3','Kasprowicza 4') )
cur.execute('SELECT * FROM pracownicy')
print(cur.fetchall())