# a while loop tells python to excute a certain statement of block of statements until a condition(len(numbers) > 0:) is false
# as long as the condition being execute the loop will run

# i = 0
# numbers = [0,1,2,3,4,5]
# while len(numbers) > 0:
#     print(numbers)
#     # to increament the i in order to stop it from continously running
#     numbers.pop()
#
# while i < 10:
#     print("Lydia")
#     i = i+1
# != means
passwordSaved = "1234"
tries = 1
password = input("Enter Your Password ")
while password != "1234" and tries <4:
    maxTries  = 1
    password = input("Please enter the correct password"+ maxTries + "t")
    tries +=1

if tries >=3:
    print("Your Card is withheld")
else:
    print(" Hurray correct password entered!")


