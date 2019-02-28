def gross(basicSalary,housingAllowance,travelAllowance,airtime):
    grossSalary = basicSalary+housingAllowance+travelAllowance+airtime
    return grossSalary

def deductions(nhif,nssf,paye,tax):
    totalDeductions = nhif+nssf+paye+tax
    return totalDeductions

def nhif (grossSalary):
    if grossSalary ==0 and grossSalary<= 5999:
        return 150
    elif grossSalary ==6000 and grossSalary<=7999:
        return 300
    elif grossSalary ==8000 and grossSalary<=11999:
        return 400
    elif grossSalary ==12000 and grossSalary<=14999:
        return 500
    elif grossSalary ==15000 and grossSalary<=19999:
        return 600
    elif grossSalary ==20000 and grossSalary<=24999:
        return 750
    elif grossSalary ==25000 and grossSalary<=29999:
        return 850
    elif grossSalary ==30000 and grossSalary<=34999:
        return 900
    elif grossSalary ==35000 and grossSalary<=39999:
        return 950
    elif grossSalary ==40000 and grossSalary<=44999:
        return 1000
    elif grossSalary ==45000 and grossSalary<=49999:
        return 1200
    elif grossSalary ==50000 and grossSalary<=59999:
        return 1200
    elif grossSalary ==60000 and grossSalary<=69999:
        return 1300
    elif grossSalary ==70000 and grossSalary<=79999:
        return 1400
    elif grossSalary ==80000 and grossSalary<=89999:
        return 1500
    elif grossSalary ==90000 and grossSalary<=99999:
        return 1600
    elif grossSalary >= 100000:
        return 1700
    else:
        return "Enter a valid Amount"



def paye(gross):
    if gross <= 147580:
        return (gross * 0.1)
    if gross ==147581
        return
    if gross <= 147580:
        return (gross * 0.1)
    if gross <= 147580:
        return (gross * 0.



