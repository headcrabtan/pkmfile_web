# -*-coding: cp949 -*-
from pokeclass import pokeclass

def process(hexvalue):
	pokemon = pokeclass()
	pokemon.pid = hexvalue[3]+hexvalue[2]+hexvalue[1]+hexvalue[0]
	pokemon.pokedexid = hexvalue[9]+hexvalue[8]
	pokemon.held_item = hexvalue[11]+hexvalue[10]
	pokemon.OT_id = hexvalue[13]+hexvalue[12]
	pokemon.OT_sid = hexvalue[15]+hexvalue[14]
	pokemon.exp = hexvalue[19]+hexvalue[18]+hexvalue[17]+hexvalue[16]
	pokemon.friendship = hexvalue[20]
	pokemon.ability = hexvalue[21]
	pokemon.markings = hexvalue[22]
	pokemon.origin_lang = hexvalue[23]
	pokemon.HP_EV = hexvalue[24]
	pokemon.ATK_EV = hexvalue[25]
	pokemon.DEF_EV = hexvalue[26]
	pokemon.SPD_EV = hexvalue[27]
	pokemon.SPATK_EV = hexvalue[28]
	pokemon.SPDEF_EV = hexvalue[29]
	pokemon.cool_val = hexvalue[30]
	pokemon.beauty_val = hexvalue[31]
	pokemon.cute_val = hexvalue[32]
	pokemon.smart_val = hexvalue[33]
	pokemon.tough_val = hexvalue[34]
	pokemon.sheen_val = hexvalue[35]
	pokemon.sinnoh_rib1 = hexvalue[37]+hexvalue[36]
	pokemon.sinnoh_rib2 = hexvalue[39]+hexvalue[38]
	pokemon.move_1 = hexvalue[41]+hexvalue[40]
	pokemon.move_2 = hexvalue[43]+hexvalue[42]
	pokemon.move_3 = hexvalue[45]+hexvalue[44]
	pokemon.move_4 = hexvalue[47]+hexvalue[46]
	pokemon.move_1pp = hexvalue[48]
	pokemon.move_2pp = hexvalue[49]
	pokemon.move_3pp = hexvalue[50]
	pokemon.move_4pp = hexvalue[51]
	pokemon.move1_ppup = hexvalue[52]
	pokemon.move2_ppup = hexvalue[53]
	pokemon.move3_ppup = hexvalue[54]
	pokemon.move4_ppup = hexvalue[55]
	pokemon.IVcalcsum = bin(int(hexvalue[59]+hexvalue[58]+hexvalue[57]+hexvalue[56],16))[2:].zfill(32)
	pokemon.HP_IV = hex(int(pokemon.IVcalcsum[27:], 2)).replace('0x',"")
	pokemon.ATK_IV = hex(int(pokemon.IVcalcsum[22:27], 2)).replace('0x',"")
	pokemon.DEF_IV = hex(int(pokemon.IVcalcsum[17:22], 2)).replace('0x',"")
	pokemon.SPD_IV = hex(int(pokemon.IVcalcsum[12:17], 2)).replace('0x',"")
	pokemon.SPATK_IV = hex(int(pokemon.IVcalcsum[7:12], 2)).replace('0x',"")
	pokemon.SPDEF_IV = hex(int(pokemon.IVcalcsum[2:7], 2)).replace('0x',"")
	pokemon.isegg_flag = hex(int(pokemon.IVcalcsum[1:2], 2)).replace('0x',"")
	pokemon.isnamed_flag = hex(int(pokemon.IVcalcsum[:1], 2)).replace('0x',"")
	pokemon.hoenn_rib1 = hexvalue[61]+hexvalue[60]
	pokemon.hoenn_rib2 = hexvalue[63]+hexvalue[62]
	pokemon.gender_FCsum = bin(int(hexvalue[64],16))[2:].zfill(8)
	pokemon.fateful_encounter = hex(int(pokemon.gender_FCsum[7:8], 2)).replace('0x',"")
	pokemon.female = hex(int(pokemon.gender_FCsum[6:7], 2)).replace('0x',"")
	pokemon.genderless = hex(int(pokemon.gender_FCsum[5:6], 2)).replace('0x',"")
	pokemon.alternate_forms = hex(int((pokemon.gender_FCsum[0:5])[::-1], 2)).replace('0x',"") 
	pokemon.nature = hexvalue[65]
	pokemon.hasdreamabil_flag = (bin(int(hexvalue[66]))[2:].zfill(8))[7:8]
	pokemon.ns_poke = (bin(int(hexvalue[66]))[2:].zfill(8))[6:7]
	pokemon.counter = 93
	for a in hexvalue[93:71]:
		pokemon.nickname += a
		pokemon.counter -= 1
	'''pokemon.hometown = 
	pokemon.sinnoh_rib3 = 
	pokemon.sinnoh_rib4 = 
	pokemon.OT_name = 
	pokemon.date_egg = 
	pokemon.date_met = 
	pokemon.egg_loc = 
	pokemon.met_loc = 
	pokemon.pokerus = 
	pokemon.pokeball = 
	pokemon.met_lv = 
	pokemon.OT_gender_flg = 
	pokemon.encounter_type = '''
	return pokemon
