
a = int(input("Enter a Number "))

# if a % 2 ==0 and a % 4 !=0:
#     print("Number is even ")
# elif a % 2!=0:
#     print("Number is odd ")
# elif a % 4 ==0:
#     print("Number is divisible by 4 and an even number ")
# else:
#     print("Enter another number ")


def determineTypeofNumber(num):
    if num %4 ==0:
        return ("Number is a multiple of 4")
    elif num % 2 ==0 :
        return ("The number is even")
    else:
        return ("number is odd")
print(determineTypeofNumber(a))



