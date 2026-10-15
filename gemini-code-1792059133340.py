# Custom Exception
class StudentNotFoundError(Exception):
    """Raised when a student ID cannot be found in records."""
    pass

def validate_age(age):
    try:
        age_int = int(age)
        if age_int <= 0 or age_int > 120:
            raise ValueError("Age must be between 1 and 120.")
        return age_int
    except ValueError as e:
        print(f"Invalid Input: {e}")
        raise
    finally:
        print("Age validation check completed.")