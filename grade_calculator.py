def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do better 🙂"
    elif marks >= 60:
        return "D", "You passed, but improvement needed ⚠️"
    else:
        return "F", "Failed. Don’t give up, try harder 💪"


# Input student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Enter between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Output
print("\nRESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
