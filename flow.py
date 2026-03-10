stu_marks = [45, 34, 37, 27, 32, 35, 23, 31, 21, 12]

even_marks = []
odd_marks = []

for mark in stu_marks:
    if mark % 2 == 0:
        even_marks.append(mark)
    else:
        odd_marks.append(mark)

print("Even Marks List:", even_marks)
print("Odd Marks List:", odd_marks)