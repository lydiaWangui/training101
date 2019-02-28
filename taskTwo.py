def largeNumber(x):
    x.sort()
    largest = x[-1]
    return largest

# def findTheLargest(x,y,z):
#     if x > y and x>z:
#         return x
#     elif y>x and y>z:
#         return y
#     elif z>y and z>x:
#         return z
#     else:
#         return "all are equal"



a = int(input("Enter a number "))
b = int(input("Enter another number "))
c = int(input("Enter another number "))

var= [a,b,c]

print("The largest variable is {}".format(largeNumber(var)))

