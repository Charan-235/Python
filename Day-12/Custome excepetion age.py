class InvalidAgeError(Exception):
    pass
def validate_age(age):
    if age < 18 or age > 100:
        raise InvalidAgeError("Invalid age: must be between 18 and 100")
    return age
try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Valid age:",age)
except InvalidAgeError as e:
    print("Error:", e)
