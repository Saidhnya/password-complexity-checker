import re

def assess_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.match('[\W_]', password))

    score = 0

    # Length
    if length >= 8:
        score += 2
    elif 6 <= length < 8:
        score += 1

    # Mix of uppercase and lowercase letters
    if has_uppercase and has_lowercase:
        score += 2

    # Presence of digits
    if has_digit:
        score += 2

    # Presence of special characters
    if has_special:
        score += 3

    # Feedback
    if score >= 8:
        feedback = "Strong"
    elif 5 <= score < 8:
        feedback = "Moderate"
    else:
        feedback = "Weak"

    return feedback

# Test the function
password = input("Enter a password to assess its strength: ")
strength = assess_password_strength(password)
print(f"The strength of the password '{password}' is: {strength}")
