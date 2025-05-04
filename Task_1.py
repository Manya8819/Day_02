marks = [
    [85, 78, 92],  # Marks of Student 1
    [76, 88, 90],  # Marks of Student 2
    [90, 91, 89]   # Marks of Student 3
]

print("Total and Average Marks:")
for i, student_marks in enumerate(marks, start=1):
    total = sum(student_marks)
    average = total / len(student_marks)
    print(f"Student {i}: Total = {total}, Average = {average:.2f}")
