# a function is a block of code used to perform a related function
# # creating or defining a function
# def chapisha(sth):
#     print(sth)
# #
# # calling or using the function
# chapisha("Lydia")
# # it becomes a function

def totalMarks(math,eng,kis,sci,ssr):
    totalMarks= math+eng+kis+sci+ssr
    return totalMarks
def average(t):
    avg = t/5
    return avg

def findGrade(average):
    if average >= 80 and average < 101:
        return ("A")
    elif average >= 70 and average < 80:
        return ("B")
    elif average >= 60 and average < 70:
        return ("C")
    elif average >= 50 and average < 60:
        return ("D")
    else:
        return ("E")