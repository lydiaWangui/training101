emptyString = ""
print(type(emptyString))
myFirstNumber = 0
emptyList = []
# noiseMakers= ["Brian" "Mike", 9, True]
daysOfTheWeek = ["Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
print(daysOfTheWeek)
numberOfDaysInAweek =len(daysOfTheWeek)
print(numberOfDaysInAweek)

# listIndexing
# firstElement
# daysOfTheWeek[0]
# lastElement
# daysOfTheWeek[len(daysOfTheWeek)-1]
thirdDayOfTheWeek=daysOfTheWeek[2]
print(thirdDayOfTheWeek)

subList = daysOfTheWeek[3:4]
print(subList)
details = ["Lydia", 30,"lwangui@generation.org", "Nairobi"]
age = details[1]
location = details[-1]

# detailsReverse= details[2::-1]
detailsReverse= details[-2:4]
# detailsReverse= details[-2::]
print("Reverse",detailsReverse)

numbers = [0,1,2,3,4,5,6,7,8,9,10]
# python counts exclusive the number after the colon
subNum = numbers[-3:-1]
print(subNum)


daysOfTheWeek.append("Val")
daysOfTheWeek.append(numbers)
# append doesn't return anything
# print(daysOfTheWeek[-1])
# clear removes elements from the list
# daysOfTheWeek.clear()
daysOfTheWeek.extend(numbers)
print(daysOfTheWeek)


list1 = [0,1]
list2 = [2,3]
list3 =list1+list2

list1.extend(list2)
print(list1)
print(list3)