
import sqlite3


def pokedatashift () :
	
	pokefile = open(r"C:\Users\jwsuh\Desktop\damcalc\data.txt",'rt')
	
	
	
	
	pokedatabase = sqlite3.connect(r"C:\Users\jwsuh\Desktop\damcalc\poke.db")
	cursor = pokedatabase.cursor()
	cursor.execute("CREATE TABLE pokemon(dexnum,name,hp,atk,def,satk,sdef,spd)")
	for i in range(659):
	 pokestring = pokefile.readline()
	 sepered = pokestring.split()
	 cursor.execute("INSERT INTO pokemon VALUES(?,?,?,?,?,?,?,?);",(sepered[0],sepered[1],sepered[2],sepered[3],sepered[4],sepered[5],sepered[6],sepered[7]))
	 pokedatabase.commit()
	print('SUCKSEX!')
	cursor.execute('SELECT * FROM pokemon')
	print (cursor.fetchall())





pokedatashift()

	
	
	
	
	
	
	













