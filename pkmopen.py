# -*- coding: utf-8 -*-
def pkmtohex(path):
	hexvalue = []
	pkmfile = open(path,'rb')
	while True:
		buffhex = pkmfile.read(16)
		bufflen = len(buffhex)

		if bufflen == 0: break

		for i in range(bufflen):
			hexvalue.append("%02X" % (ord(buffhex[i])))

	if not len(hexvalue) == 136: return 'n/a'

	for a in range(136):
		hexvalue[a] = hexvalue[a].replace('0x','')
		#hexvalue[a] = int(hexvalue[a], 16) hex to int

	return hexvalue





