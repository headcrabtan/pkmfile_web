# -*-coding: cp949 -*-
from pkmtohex import pkmtohex
import pokeclass
from pkm_converter import process

val = pkmtohex(r'C:\Users\jwsuh\Desktop\unknown.pkm')
poke = process(val)

print bin(int(val[64],16))[2:].zfill(8)
print poke.female
print poke.genderless
print poke.fateful_encounter
