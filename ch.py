def calculate_grade(score):
    if score < 0 or score > 100:
        return "Error: Score is out of range (0-100)"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
try:
    input_score = float(input("Enter a score between 0 and 100: "))
    grade = calculate_grade(input_score)
    print(f"Grade: {grade}")
except ValueError:
    print("Error: Please enter a valid numeric score.")
