#Joshua Carter
#03/18/2024
#P3HW1
#Salary Calc

'''
#Pseudocode

Input name
Display "Enter employee's name: "
Input hours
Display "Enter number of hours worked: "
Input payrate
Display "Enter employee's pay rate: "

If hours > 40
    othours = hours - 40
    reghours = 40
else
    othours = 0
    reghours = hours
otpay = othours * (payrate * 1.5)
regpay = reghours * payrate
gpay = regpay + otpay

Display "---------------------------------"
Display "Employee name:", name
Display " "
Display "'Hours Worked:, Pay Rate:, Overtime:, Overtime Pay:, RegHour Pay:, Gross Pay:'"
Display "-----------------------------------------------------------------------------"
Display "hours, payrate, othours, oypay, regpay, gpay"
'''

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))

if hours > 40:
    othours = hours - 40
    reghours = 40
else:
    othours = 0
    reghours = hours

otpay = othours * (payrate * 1.5)
regpay = reghours * payrate
gpay = regpay + otpay


print(f"---------------------------------")
print(f"Employee name:", name)
print()
print(f"{'Hours Worked':<13}{'Pay Rate':<10}{'Overtime':<10}{'Overtime Pay':<14}{'RegHour Pay':<14}{'Gross Pay':<13}")
print(f"-----------------------------------------------------------------------------")
print(f"{hours:<13}{payrate:<10}{othours:<10}{otpay:<14}{regpay:<14}{gpay:<13}")


