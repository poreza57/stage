f = open("zoo_clear.txt", "r" )
zoo_clear = f.read()

clear=""
key = 5

for letter in range (0 ,len(zoo_clear)):
	#print (ord(zoo_clear[letter]))	
	
	if (ord (zoo_clear[letter]) - key >=65):
		clear = clear + chr(ord(zoo_clear[letter])-key)
	else:
		index = (ord(zoo_clear[letter]) - key) - 65
		clear = clear + chr(91 + index)
		

print (clear)