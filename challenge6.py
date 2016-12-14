f = open ( "secret.txt", "r")
secret = f.read()

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = 3

#first secret letter
#print (secret[0])

#Current position in the alpha
current_position = alpha.find(secret[0])

#position of the clear letter
new_position = alpha.find(secret[0]) - key


#print (alpha[new_position])
#print(secret.find('H'))
clear = ""
for lettre in range (0 ,len(secret)):
	#print (secret[lettre])
	#print (alpha.find(secret[lettre]))
	#print (alpha.find(secret[lettre]) - key)
	#print (alpha[alpha.find(secret[lettre]) - key])
     clear = clear+ alpha[alpha.find(secret[lettre]) - key]
print (clear)


f.close()