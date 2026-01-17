def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    vowels = "aeiou"

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single alphabet letter.")
    elif letter in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Call the function
check_letter()

def check_voting_eligibility():
    try:
        # اطلب من المستخدم إدخال عمره
        age = int(input("Please enter your age: "))

        # تحقق أن العمر ليس سالب
        if age < 0:
            print("Age cannot be negative.")
        else:
            voting_age = 18  # العمر القانوني للتصويت
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote yet.")
    except ValueError:
        # لو المستخدم كتب شيء غير رقم
        print("Invalid input. Please enter a valid number.")

# Call the function
check_voting_eligibility()
def check_voting_eligibility():
    age_input = input("Please enter your age: ")

    # Check if the input is digits only
    if age_input.isdigit():
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative.")
        else:
            voting_age = 18
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote yet.")
    else:
        print("Invalid input. Please enter a valid number.")

def calculate_dog_years():
    # Prompt the user to enter a dog's age
    dog_age = int(input("Input a dog's age: "))

    # Apply the rules for dog years calculation
    if dog_age <= 0:
        print("Age must be a positive number.")
    elif dog_age <= 2:
        dog_years = dog_age * 10
        print(f"The dog's age in dog years is {dog_years}.")
    else:
        dog_years = 20 + (dog_age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")

# Call the function
calculate_dog_years()
