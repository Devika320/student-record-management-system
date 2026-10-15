import csv
import json
import os

# Function with default parameters and return values
def add_student(student_list, student_id, name, age, course):
    student = {
        "id": student_id,
        "name": name,
        "age": int(age),
        "course": course
    }
    student_list.append(student)
    return student_list

# Lambda function and List Comprehension for filtering/searching
search_student = lambda students, target_id: [s for s in students if s["id"] == target_id]

# File Handling: Saving to CSV
def save_to_csv(filename, students):
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ["id", "name", "age", "course"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print("Data successfully saved to CSV.")
    except IOError as e:
        print(f"Error writing to file: {e}")

# File Handling: Loading from JSON
def load_from_json(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, mode='r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
        return []