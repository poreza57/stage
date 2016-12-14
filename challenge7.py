secret = "FGHIJKLMNOPQRSTUVWXYZABCDE"
clear=""
key = 5

for letter in range (0 ,len(secret)):
	#print (ord(secret[letter]))	
	
	if (ord (secret[letter]) - key >=65):
		clear = clear + chr(ord(secret[letter])-key)
	else:
		index = (ord(secret[letter]) - key) - 65
		clear = clear + chr(91 + index)
		

print (clear)