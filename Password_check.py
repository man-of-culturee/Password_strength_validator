def check_password(password):
    min_length = 8
    special_chars = {"@", "#", "$", "%"}

    digit_count = 0
    lower_count = 0
    upper_count = 0
    special_count = 0

    feedback = []
    score = 0

    # Checking if the Length of password is <= 84
    if len(password) >= min_length:
        score += 1
    else:
        feedback.append("At least 8 characters required")

    # Making sure that no consecutive identical characters are inside password
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            feedback.append("No consecutive identical characters allowed")
            break

    # Count each type character
    for char in password:
        if char.isdigit():
            digit_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        elif char in special_chars:
            special_count += 1

    # Check if password has more than 2 Numeric characters
    if digit_count >= 2:
        score += 1
    else:
        feedback.append("At least 2 digits required")

    # Check if password has at least 1 Special Character
    if special_count >= 1:
        score += 1
    else:
        feedback.append("Include at least 1 special character (@,#,$,%)")

    # Check if password has at least 1 Lowercase Character
    if lower_count >= 1:
        score += 1
    else:
        feedback.append("Include at least 1 lowercase letter")

    # Check if password has at least 1 Uppercase Character
    if upper_count >= 1:
        score += 1
    else:
        feedback.append("Include at least 1 uppercase letter")

    return score, feedback
