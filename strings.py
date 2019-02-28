# a string is an array of characters.
# they are used to paas ing=fo acrross python.

myFirstString = "hello world."
print(myFirstString.capitalize())
# makes every letter of the string capital
print(myFirstString.upper())
# makes every letter of the string lower case
print(myFirstString.lower())
# counts the number of characters
print(myFirstString.count('o'))

# joining two strings/ multiple assignment
firstName,secondName,= "wangui" ,"lydia"
print(firstName)
print(secondName)
# to put a space betwen tha names, add a space quotes betweem the names as shown below/ concutnate two strings.
fullName = firstName +" "+ secondName
print(fullName)

# finding the last and firstcharacter
firstLetter= fullName[0]
# lastLetter=fullName[-1]
lastLetter=fullName[len(fullName)-1]
print(lastLetter.upper())
print(firstLetter.upper())
# determining the length of a string
lengthOfMyFullName=len(fullName)
print(lengthOfMyFullName)
