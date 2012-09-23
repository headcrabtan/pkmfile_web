# -*-coding: cp949 -*-
from pkmtohex import pkmtohex
import pokeclass
#from pkm_converter import process

val = pkmtohex(r'C:\Users\jwsuh\Desktop\nintales.pkm')
print  val[0x38],val[0x39],val[0x3A],val[0x3B]


