f = open("zoo_clear.txt", "r" )
zoo_clear = f.read()

secret=""
key = 5

for letter in range (0 ,len(zoo_clear)):
	#print(ord(zoo_clear[letter]))	
	secret = secret + chr(ord(zoo_clear[letter]) + key )

		

print (secret)

f.close()