#Open file secret.txt in read
f = open("secret.txt", "r")

#Set variable with file content
secret = f.read()

#Alphabet
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Clear message
clear = ''

#Key to read the message
key = 3

#For each letter of the secret message
for a in range(0,len(secret)):
	#secret[a] returns the letter at the position "a" from the secret message
	#alpha.find() returns the position of a letter in the alphabet
	if (alpha.find(secret[a]) - key > -1):
		#Get the letter encrypted in clear and write it in the variable clear
		clear = clear + alpha[alpha.find(secret[a]) - key]
	else:
		index = alpha.find(secret[a]) - key
		clear = clear + alpha[26 + index]
		
#Display the message in clear
print (clear)

#Open file secret.txt
f.close()