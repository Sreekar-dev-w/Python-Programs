password = input("Enter your password: ")

upper = lower = digit = special = False
special_chars = "!@#$%^&*()_+-"

if len(password) < 8:
    print("Weak: Minimum 8 chars reqd")
else:
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        elif ch in special_chars:
            special = True

    if upper and lower and digit and special:
        print("Strong Password 💪")
    else:
        print("Medium Password ⚠️")
