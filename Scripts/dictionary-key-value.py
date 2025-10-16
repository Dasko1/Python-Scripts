# Enter students' name and score (mark) and compare!

marks = {}

for i in range(1):
    student_name1 = input("Enter first student's name: ")
    student_mark1 = input("Enter first student's mark: ")
    
    student_name2 = input("Enter second student's name: ")
    student_mark2 = input("Enter second student's mark: ")

    marks[student_name1] = student_mark1
    marks[student_name2] = student_mark2

print(marks)
print(student_name1 + " got a score of: " + marks[student_name1])
