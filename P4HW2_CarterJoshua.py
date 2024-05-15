#Joshua Carter
#04/8/2024
#P4HW2
#Salary Calc w loops

'''

numemp = 0
totalOt = 0
totalreg = 0
totalgross = 0

input name 
Display "Enter employee's name or 'Done' to terminate: "

while name != "Done"
    get payrate
    get hours
    calc of pay reghours*
    (loop is broken)<-add 1 to numemp (create)
    add 1 to numemp
    totalot += otpay
    if hours > 40:
        othours = hours - 40
        reghours = 40
    else
        othours = 0
        reghours = hours
    otpay = othours * (payrate * 1.5)
    regpay = reghours * payrate
    gpay = regpay + otpay
    totalOt += otpay 
    totalreg += regpay
    totalgross += gpay

    Display "Employee name:", name
    Display "Hours worked", "Pay Rate", "Overtime", "Overtime Pay", "RegHour Pay", "Gross Pay"
    Display hours, payrate, othours, otpay, regpay, gpay

    input name
    Display "Enter employee's name or 'Done' to terminate: "

Display "Total overtime pay: $",totalOt
Display "Total regular pay: $",totalreg
Display Total gross pay: $",totalgross




'''




numemp = 0
totalOt = 0
totalreg = 0
totalgross = 0

name = input("Enter employee's name or 'Done' to terminate: ")

while name != 'Done':
    hours = float(input(f"How many hours did {name} work? : "))
    payrate = float(input(f"What is {name}'s pay rate: "))
    numemp = numemp + 1
    if hours > 40:
        othours = hours - 40
        reghours = 40
    else:
        othours = 0
        reghours = hours
    otpay = othours * (payrate * 1.5)
    regpay = reghours * payrate
    gpay = regpay + otpay
    totalOt += otpay 
    totalreg += regpay
    totalgross += gpay
    
    print(f"---------------------------------")
    print(f"Employee name:", name)
    print()
    print(f"{'Hours Worked':<13}{'Pay Rate':<10}{'Overtime':<10}{'Overtime Pay':<14}{'RegHour Pay':<14}{'Gross Pay':<13}")
    print(f"-----------------------------------------------------------------------------")
    print(f"{hours:<13}{payrate:<10}{othours:<10}{otpay:<14}{regpay:<14}{gpay:<13}")
    print()

    name = input("Enter employee's name or 'Done' to terminate: ")

print()
print(f'Total number of employees entered: {numemp}')
print(f'Total amount paid for overtime: ${totalOt:.2f}')
print(f'Total amount paid for regular hours: ${totalreg:.2f}')
print(f'Total amount paid in gross: ${totalgross:.2f}')




   



    

    







