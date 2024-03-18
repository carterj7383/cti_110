#Joshua Carter
#03/06/2024
#P2HW2
#User input added to list and pulling min/max/len/avg from list

test_grades = []

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

test_grades.append(grade1)
test_grades.append(grade2)
test_grades.append(grade3)
test_grades.append(grade4)
test_grades.append(grade5)
test_grades.append(grade6)

lowest_grade = min(test_grades)
highest_grade = max(test_grades)
sum_grades = sum(test_grades)
mod_nums = len(test_grades)
avg_grades = sum_grades / mod_nums

print()
print("------------Results------------")
print(f"Lowest Grade:   {lowest_grade:.2f}")
print(f"Highest Grade:  {highest_grade:.2f}")
print(f"Sum of Grades:  {sum_grades:.2f}")
print(f"Average:        {avg_grades:.2f}")
print("-------------------------------")




    
