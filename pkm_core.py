# -*-coding: cp949 -*-
from pkmtohex import pkmtohex
import pokeclass
from pkm_converter import process

val = pkmtohex(r'C:\Users\jwsuh\Desktop\ninetales2.pkm')
poke = process(val)

print poke.nickname