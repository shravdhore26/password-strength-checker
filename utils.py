import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def suggest_password(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters")

    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letter")

    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letter")

    if not any(c.isdigit() for c in password):
        suggestions.append("Add a number")

    if not any(c in "@#$%^&*" for c in password):
        suggestions.append("Add special character")

    return suggestions


def save_to_file(password, strength):
    with open("history.txt", "a") as f:
        f.write(f"{password} -> {strength}\n")