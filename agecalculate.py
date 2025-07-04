from datetime import datetime

def age_calculator():
    current_year = datetime.now().year

    print("🧮 Welcome to the Age Calculator!")

    birth_year = int(input("Enter your birth year (e.g., 2008): "))

    if birth_year > current_year:
        print("❌ Birth year cannot be in the future!")
    elif birth_year < 1900:
        print("❌ That birth year seems too far in the past.")
    else:
        age = current_year - birth_year
        print(f"🎉 You are {age} years old in {current_year}.")

age_calculator()
