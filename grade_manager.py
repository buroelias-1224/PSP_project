def get_valid_input(prompt, min_val, max_val, is_int=False):
    """
    Validates user input to ensure it is a number within the specified range.
    """
    while True:
        try:
            value = float(input(prompt)) if not is_int else int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Invalid input! Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_grade_and_points(mark):
    """
    Returns the letter grade and the corresponding grade point based on the specified scale.
    """
    if mark >= 90:
        return 'A+', 4.00
    elif mark >= 85:
        return 'A', 4.00
    elif mark >= 80:
        return 'A-', 3.75
    elif mark >= 75:
        return 'B+', 3.50
    elif mark >= 65:
        return 'B', 3.00
    elif mark >= 60:
        return 'B-', 2.75
    elif mark >= 55:
        return 'C+', 2.50
    elif mark >= 50:
        return 'C', 2.00
    elif mark >= 45:
        return 'C-', 1.75
    elif mark >= 40:
        return 'D', 1.00
    else:
        return 'F', 0.00


def main():
    print("=" * 55)
    print("      STUDENT CUMULATIVE GRADE SYSTEM (GPA)")
    print("=" * 55)

    student_name = input("Enter student name: ")


    num_courses = get_valid_input("Enter the total number of courses: ", 1, 20, is_int=True)

    total_credit_hours = 0
    total_quality_points = 0

    print("\n--- Enter Course Details ---")
    for i in range(1, num_courses + 1):
        print(f"\nCourse {i}:")
        course_name = input("  Enter course name (or press Enter to skip): ") or f"Course {i}"


        credit_hours = get_valid_input(f"  Enter credit hours for {course_name} (1-6): ", 1, 6, is_int=True)


        mark = get_valid_input(f"  Enter marks for {course_name} (0-100): ", 0, 100)


        letter_grade, grade_point = get_grade_and_points(mark)


        quality_points = grade_point * credit_hours


        total_credit_hours += credit_hours
        total_quality_points += quality_points

        print(f"  -> Result: {letter_grade} ({grade_point:.2f} pts) | Quality Points: {quality_points:.2f}")

    if total_credit_hours > 0:
        final_cgpa = total_quality_points / total_credit_hours
    else:
        final_cgpa = 0.0


    print("\n" + "=" * 55)
    print(f"FINAL TRANSCRIPT FOR: {student_name.upper()}")
    print("=" * 55)
    print(f"Total Credit Hours Registered: {total_credit_hours}")
    print(f"Total Quality Points Earned:   {total_quality_points:.2f}")
    print("-" * 55)

    print(f"FINAL CUMULATIVE SCORE (CGPA): {final_cgpa:.2f}")
    print("=" * 55)


if __name__ == "__main__":
    main()