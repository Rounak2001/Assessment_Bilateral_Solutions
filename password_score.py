def password_score(password):
    score = 0
    length = len(password)

    has_digit = False
    has_symbol = False
    has_uppercase = False
    has_lowercase = False

    for char in password:
        ascii_code = ord(char)
        
        if 48 <= ord(char) <= 57: 
            has_digit = True
        elif (33 <= ascii_code <= 47) or (58 <= ascii_code <= 64) or \
             (91 <= ascii_code <= 96) or (123 <= ascii_code <= 126):
            has_symbol = True
        elif 65 <= ord(char) <= 90:  
            has_uppercase = True
       
        elif 97 <= ord(char) <= 122:
            has_lowercase = True

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1

    # Bonus for having both uppercase and lowercase
    if has_uppercase and has_lowercase:
        score += 1

    return score


password = input("Enter a Password: \n")
strength_score = password_score(password)
print("The password score is between 1-7\n")
print ("Higher the score stronger the Password\n")
print(f"The strength score of the password is: {strength_score}")




