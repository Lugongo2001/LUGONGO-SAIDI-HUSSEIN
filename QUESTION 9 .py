#Question 9: Student Records and Averages
student_records = {
    'AGE/D/2023/0020': {'name': 'Alice', 'assignment_scores': [85, 90, 78, 92]},
    'AGE/D/2023/0021': {'name': 'Bob', 'assignment_scores': [75, 80, 88, 70]},
    'AGE/D/2023/0022': {'name': 'Charlie', 'assignment_scores': [92, 95, 88, 90]}}
def calculate_average_score(records, registration_number):
    """Calculates the average assignment score for a student."""
    if registration_number in records:
        scores = records[registration_number]['assignment_scores']
        average = sum(scores) / len(scores)
        return average
    else:
        return "Student not found"
registration_number = input("Enter student registration number: ")
average_score = calculate_average_score(student_records, registration_number)
print(f"Average score for {registration_number}: {average_score}")
