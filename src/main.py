def calculate_cgpa(grade_points):
    """Calculate CGPA from a list of grade points."""
    if not grade_points:
        raise ValueError("Grade points cannot be empty.")

    if any(
        not isinstance(point, (int, float)) or point < 0 or point > 10
        for point in grade_points
    ):
        raise ValueError("Grade points must be numeric and between 0 and 10.")

    return round(sum(grade_points) / len(grade_points), 2)


def main():
    print("===== Student CGPA Performance Management System =====")

    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Student name cannot be empty.")

        values = input("Enter grade points separated by spaces (0-10): ").strip()
        if not values:
            raise ValueError("Grade points cannot be empty.")

        try:
            grade_points = [float(value) for value in values.split()]
        except ValueError as exc:
            raise ValueError("Grade points must be numeric.") from exc

        cgpa = calculate_cgpa(grade_points)

        print("\n----- Student Performance Report -----")
        print(f"Student Name: {name}")
        print(f"CGPA: {cgpa:.2f}")

        if cgpa >= 9:
            print("Performance: Excellent")
        elif cgpa >= 8:
            print("Performance: Very Good")
        elif cgpa >= 7:
            print("Performance: Good")
        elif cgpa >= 6:
            print("Performance: Satisfactory")
        else:
            print("Performance: Needs Improvement")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
