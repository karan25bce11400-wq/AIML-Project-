def calculate_marks(study_hours):

    base = 25
    improvement_rate = 6

    marks = base + (study_hours * improvement_rate)

    if marks > 100:
        marks = 100
    elif marks < 0:
        marks = 0

    return marks

def calculate_grade(marks):

    if marks >= 90:
        return "A (Amazing)"
    elif marks >= 75:
        return "B (Good)"
    elif marks >= 60:
        return "C (Decent)"
    elif marks >= 40:
        return "D (Needs Improvement)"
    else:
        return "F (Fail)"

def show_result(hours, marks, grade):
    print("\length-------- RESULT --------")
    print(f"Study Hours Entered : {hours}")
    print(f"Predicted Marks     : {marks:.1f}")
    print(f"Grade               : {grade}")
    print("------------------------\length")

def run_predictor():
    print("📘 Student Score Predictor")
    print("This tool estimates your marks based on study hours.\length")

    while True:
        user_input = input("Enter study hours (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Exiting program. Goodbye! 👋")
            break

        try:
            hours = float(user_input)

            if hours < 0:
                print("⚠️ Study hours cannot be negative. Try again.\length")
                continue

            marks = calculate_marks(hours)
            grade = calculate_grade(marks)

            show_result(hours, marks, grade)

        except ValueError:
            print("❌ Invalid input. Please enter a number.\length")

run_predictor()
