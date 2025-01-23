def get_grade_count(grade):
    while True:
        try:
            count = int(input(f"How many {grade}s did you make? : "))
            if count < 0:
                raise ValueError("Count cannot be negative.")
            return count
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative integer.")

def main():
    while True:
        try:
            num_courses = int(input("How many courses are you taking? "))
            if num_courses <= 0:
                raise ValueError("Number of courses must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    grades = {
        'A': 4.0,
        'B+': 3.5,
        'B': 3.0,
        'C+': 2.5,
        'C': 2.0,
        'D+': 1.5,
        'D': 1.0,
        'E': 0.5,
        'F': 0.0
    }

    total_points = 0
    total_courses = 0

    for grade, points in grades.items():
        count = get_grade_count(grade)
        total_points += count * points
        total_courses += count

    if total_courses != num_courses:
        print(f"Warning: The total number of courses entered ({total_courses}) does not match the number of courses you are taking ({num_courses}).")

    GPA = total_points / num_courses
    print(f"Your GPA is: {GPA:.2f}")

if __name__ == "__main__":
    main()