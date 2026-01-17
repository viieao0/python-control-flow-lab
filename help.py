

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
