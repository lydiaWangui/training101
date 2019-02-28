taskList = [23, "Jane", ["Lesson 23",560,{"currency": "KES"}],987,(76,"John")]
# Q1. determine the type of variable taskList using an inbuilt function
print(type(taskList))
# Q2. print "KES"
# get into index 2 of tasklist using the first[2],then got into index 2 of using the second[2], then found currency in the dictionary using the keyword"currency".
print(taskList[2][2]["currency"])
# Q3. Print 560
print(taskList[2][1])
# Q4. use a function to determine the length of taskList
print(len(taskList))
# Q5. Change 987 to 789 using an inbuilt function
# covert the number 987 into a string,then use:: to reverse the number then afterwards change it into a integer using int. OR you vcan pop it then insert the number required.
num=(taskList[3])
number= str(num)
print(int(number[::-1]))
# Q6.  change name "jOHN" to "Jane"
# not possible

taskListA=(taskList[4:5])
print(taskListA)
# print(taskListA.index("KES"))

print(len(taskList))

print(*taskListA, sep='\5')

