import math

def decimal_to_binary(decimal):
	blist = []
	while decimal > 0:
		if decimal % 2 == 0:
			blist.append(0);
		else:
			blist.append(1)
		
		decimal /= 2

	return blist[::-1]

def decimal_to_octal(decimal):
	olist = []
	while decimal >= 8:
		if decimal % 8 == 0:
			olist.append(0);
		else:
			olist.append(decimal % 8)
		
		decimal /= 8
	
	olist.append(decimal)
	return olist[::-1]

def decimal_to_hexadecimal(decimal):
	h = {
		0:0,
		1:1,
		2:2,
		3:3,
		4:4,
		5:5,
		6:6,
		7:7,
		8:8,
		9: 9,
		10:'A',
		11:'B',
		12:'C',
		13:'D',
		14:'E',
		15:'F',
	}
	hlist = []
	
	remainder = 0
	while decimal >= 16:
		remainder = decimal % 16
		
		if remainder == 0:
			hlist.append(h[remainder]);
		else:
			hlist.append(h[remainder])
		
		decimal /= 16
	
	hlist.append(h[decimal])
	return hlist[::-1]


def binary_to_decimal(binary):
	#assuming binary argument that is passed is a list
	total = 0
	rlist = binary[::-1]
	for i in range(len(rlist)):
		if i == 0:
			total += (rlist[i] * 1)
		else:
			total += (math.pow(2,i) * rlist[i])
	
	return total

def binary_to_octal(binary):
	olist = []
	i = 0
	while len(binary) % 3 != 0:
		binary.insert(i,0)
		i += 1
	
	j = 0
	mult = 4
	total = 0
	while j < len(binary):
		total += (binary[j] * mult)
		mult /= 2
		
		if ((j+1) % 3 == 0 and j > 0):
			olist.append(total)
			mult = 4
			total = 0
		
		j += 1
	return olist

def binary_to_hexadecimal(binary):
	h = {
		0:0,
		1:1,
		2:2,
		3:3,
		4:4,
		5:5,
		6:6,
		7:7,
		8:8,
		9: 9,
		10:'A',
		11:'B',
		12:'C',
		13:'D',
		14:'E',
		15:'F',
	}

	hlist = []
	i = 0
	while len(binary) % 4 != 0:
		binary.insert(i,0)
		i += 1
	
	j = 0
	mult = 8
	total = 0
	while j < len(binary):
		total += (binary[j] * mult)
		mult /= 2
		
		if ((j+1) % 4 == 0 and j > 0):
			hlist.append(h[total])
			mult = 8
			total = 0
		
		j += 1
	return hlist

def octal_to_binary(octal):	
	#assuming octal digits are in a list
	blist = []
	for i in range(len(octal)):
		dlist = decimal_to_binary(octal[i])
		i = 0
		if len(dlist) < 3:
			while len(dlist) < 3:
				dlist.insert(i,0);
				i += 1
			blist += dlist
		else:
			blist += dlist
			
	return blist

def octal_to_decimal(octal):
	return binary_to_decimal(octal_to_binary(octal))

def octal_to_hexadecimal(octal):
	return binary_to_hexadecimal(octal_to_binary(octal))

def hexadecimal_to_binary(hexadecimal):
	h = {
		0:0,
		1:1,
		2:2,
		3:3,
		4:4,
		5:5,
		6:6,
		7:7,
		8:8,
		9:9,
		'A': 10,
		'B': 11,
		'C': 12,
		'D': 13,
		'E': 14,
		'F': 15,
	}
	
	hlist = []
	for i in range(len(hexadecimal)):
		dlist =  decimal_to_binary(h[hexadecimal[i]])
		
		i = 0
		if len(dlist) < 4:
			while len(dlist) < 4:
				hlist.insert(i,0);
				i += 1
			hlist += dlist
		else:
			hlist += dlist
			
	return hlist

def hexadecimal_to_decimal(hexadecimal):
	return binary_to_decimal(hexadecimal_to_binary(hexadecimal))

def hexadecimal_to_octal(hexadecimal):
	return binary_to_octal(hexadecimal_to_binary(hexadecimal))
	