import sqlite3

def getdb(serch):
 connect = sqlite.connect('./poke.db')
 pokedb = connect.cursor()
 pokedb.execute("SELECT * FROM POKE ")
 print (pokedb)

getdb(8)
 
