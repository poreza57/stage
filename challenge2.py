setsofplain = 3*4
hat = 3
protectiongloves = 2
wintercloack = 3
basegallions = 22
uniform = setsofplain + hat + protectiongloves + wintercloack
gallions = basegallions-uniform
print ("Mathis,you spent " +str(uniform)+ " gallions in your uniforms")
print ("Mathis you have " +str(gallions)+ " gallions.")
if uniform < 22:
	print ("Mathis, you have " +str(gallions)+ " galleons to buy candies")

if gallions > 1.50:
	print ("You can buy choclates frogs or 2 beans")
	if gallions > 2.25:
		print ("you can buy choclates frogs and beans")
	if gallions > 0.75 > 1.50:
		print ("you can buy beans")