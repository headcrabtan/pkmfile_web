# -*-coding: cp949 -*-
from pokeclass import pokeclass

def process(hexvalue):
	pokemon = pokeclass()
	pokemon.pid = hexvalue[3]+hexvalue[2]+hexvalue[1]+hexvalue[0]
	pokemon.pokedexid = 
	return pokemon
