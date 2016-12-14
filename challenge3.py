print ("List of the gryffindor students:")
griffindorList = ["Hermione Granger","Ronald Weasley","Harry Potter","Lavande Brown"]
for student in griffindorList:

    print (student)

print ("")
griffindorList.append("Neville Londubat")

print ("List of the gryffindor students:")
for student in griffindorList:

    print (student)

print ("")

print ("List of the student sorted alphabtically")

griffindorList.sort()

for student in griffindorList:

    print (student)

print ("")

print ("List of the student sorted alphabtically in dexcending")

griffindorList.reverse()

for student in griffindorList:

    print (student)

print ("")

print ("List of the students without Lavande Brown:")

griffindorList.remove ("Lavande Brown")

for student in griffindorList:

    print (student)

	
#print (griffindorList)
#print ("List of the griffindor students:")
#griffindorList.append ("Neville londubat")
#print (griffindorList)
#print ("List of the students sorted alphabetically:")
#griffindorList.sort()
#print (griffindorList)
#print ("List of students sorted alphabtically in descending order:")
#griffindorList.reverse()
#print (griffindorList)
#print ("list of the student without Lavende Brown:")
#griffindorList.remove ("Lavande Brown")
#print (griffindorList)