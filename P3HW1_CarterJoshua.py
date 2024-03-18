#Joshua Carter
#03/15/2024
#P3HW1
#Debug lists and if/else/elif statements


# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
gradeSum = sum(grades)
modNums = len(grades)
gradeAvg = gradeSum / modNums

# determine letter grade for average


if gradeAvg >= 90:
    letterGrade = "A"
elif gradeAvg >= 80:
    letterGrade = "B"
elif gradeAvg >= 70:
    letterGrade = "C"
elif gradeAvg >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print()
print("------------Results------------")
print(f"Lowest Grade:   {low:.2f}")
print(f"Highest Grade:  {high:.2f}")
print(f"Sum of Grades:  {gradeSum:.2f}")
print(f"Average:        {gradeAvg:.2f}")
print("-------------------------------")
print(f"Your grade is: {letterGrade}")





