import string

pw = input("Enter a password: ")


messages = []
score = 0


if len(pw) >= 8:
    score += 2
else:
    messages.append("Your password needs to be at least 8 characters long.")


if any(char.islower() for char in pw):
    score += 2
else:
    messages.append("Your password needs at least one lowercase letter.")


if any(char.isupper() for char in pw):
    score += 2
else:
    messages.append("Your password needs at least one uppercase letter.")


if any(char.isdigit() for char in pw):
    score += 2
else:
    messages.append("Your password needs at least one digit.")


if any(char in string.punctuation for char in pw):
    score += 2
else:
    messages.append("Your password needs at least one special character (like @, #, $, etc.).")

# Step 3: Show result
if not messages:
    print("✅ Your password is strong! 💪")
else:
    for message in messages:
        print("❗", message)

# Bonus: Password strength meter
print(f"\n🔋 Password Strength Score: {score}/10")
if score == 10:
    print("Excellent! 🔥")
elif score >= 8:
    print("Good, but you could improve it slightly. 😊")
elif score >= 5:
    print("Weak, consider making it stronger. ⚠️")
else:
    print("Very weak password. ❌")

