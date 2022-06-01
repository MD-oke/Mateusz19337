import sqlite3

conn = sqlite3.connect('database.db')
print("BD otwarta")

conn.execute('CREATE TABLE pracownicy (imieinazwisko TEXT , nrpracownika TEXT , adres TEXT)')
print("Tabela utworzona")
cur = conn.cursor()
cur.execute("INSERT INTO pracownicy (imieinazwisko,nrpracownika,adres) Values (?,?,?)",('mateuszdyrdowski','20','polna2'))
cur.execute('SELECT * FROM pracownicy')
print(cur.fetchall())
conn.close()