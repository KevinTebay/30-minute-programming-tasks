# Sample data (for testing, replace these with actual class data as needed)
StudentName = ["Alice", "Bob", "Charlie", "David"]
StudentMark = [
    [80, 90, 70],  # Alice's marks
    [60, 55, 58],  # Bob's marks
    [45, 50, 42],  # Charlie's marks
    [30, 35, 25]   # David's marks
]
ClassSize = len(StudentName)
SubjectNo = len(StudentMark[0])

# Initialize counters for grades
distinctions = 0
merits = 0
passes = 0
fails = 0

# Process each student
for i in range(ClassSize):
    total_mark = 0

    # Calculate the total mark for the current student
    for j in range(SubjectNo):
        total_mark += StudentMark[i][j]

    # Calculate average mark, rounded to nearest whole number
    average_mark = round(total_mark / SubjectNo)

    # Determine grade based on average mark
    if average_mark >= 70:
        grade = "distinction"
        distinctions += 1
    elif average_mark >= 55:
        grade = "merit"
        merits += 1
    elif average_mark >= 40:
        grade = "pass"
        passes += 1
    else:
        grade = "fail"
        fails += 1

    # Output student details
    print("Name:", StudentName[i])
    print("Total Mark:", total_mark)
    print("Average Mark:", average_mark)
    print("Grade Awarded:", grade)
    print()

# Output overall grade counts for the class
print("Total Distinctions:", distinctions)
print("Total Merits:", merits)
print("Total Passes:", passes)
print("Total Fails:", fails)
