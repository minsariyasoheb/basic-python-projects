marks = []
subjects = ["Eng", "Math", "Sci"]
grades = []
total_marks = 0

# Input marks and assign subject-wise grades
for subject in subjects:
    while True:
        mark = int(input(f"Enter marks for {subject}: "))
        if mark < 0 or mark > 100:
            print("Invalid input. Please enter marks between 0 and 100.")
        else:
            marks.append(mark)
            if mark >= 90:
                grades.append("A")
            elif mark >= 75:
                grades.append("B")
            elif mark >= 60:
                grades.append("C")
            elif mark >= 35:
                grades.append("D")
            else:
                grades.append("F")
            break

# Calculate total and percentage
total_marks = sum(marks)
percentage = (total_marks / 300) * 100

# Determine overall grade
if percentage >= 90:
    overall_grade = "A"
elif percentage >= 75:
    overall_grade = "B"
elif percentage >= 60:
    overall_grade = "C"
elif percentage >= 35:
    overall_grade = "D"
else:
    overall_grade = "F"

# Display results
print("\n\t\tResult")
print("Subject\t\tMarks\t\tGrade")
for i in range(3):
    print(f"{subjects[i]}\t->\t{marks[i]}\t\t{grades[i]}")

print("=====================================")
print(f"Total:\t\t{total_marks} / 300")
print(f"Percentage:\t{percentage:.2f}%\t\t{overall_grade}")