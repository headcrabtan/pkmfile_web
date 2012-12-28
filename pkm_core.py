# -*-coding: cp949 -*-
from pkmtohex import pkmtohex
import pokeclass
from pkm_converter import process

def pkmparse(path)
	val = pkmtohex(path)
	poke = process(val)
	return poke
pkmparse('C:\Keldeo.pkm')
