import random
import datetime

def NumberGuessingGame():
    attempts = 0
    max_attempts = 10

    random_number = random.randint(1, 100)
    
    print("\nRules:")
    print("\n1) I'm thinking of a number between 1 and 100.")
    print(f"2) You have {max_attempts} attempts to guess the correct number.")

    while attempts < max_attempts:
        try:
            user_guess = int(input("\nAttempt {}: Enter your guess: ".format(attempts + 1)))

            if user_guess < 1 or user_guess > 100:
                print("Your guess should be between 1 and 100.")
            elif user_guess < random_number:
                print("Too low!")
            elif user_guess > random_number:
                print("Too high!")
            else:
                print(f"\nCongratulations! You guessed the number {random_number} correctly in {attempts + 1} attempts.")
                return True
            
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"\nGame over! The number was {random_number}.")
    return False

# Driver Code
print("\n----------- Number Guessing Game! -----------")
name = input("Enter Your Name: ")
print("\n--------------- WELCOME", name.upper(), "--------------")
    
while True:
    print("\nDate:", datetime.date.today())
    print("Time:", datetime.datetime.now().time())
    
    if not NumberGuessingGame():
        break
        
    play_again = input("\nDo you want to play again? (yes/no): ")
    while play_again.lower() not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to play again? (yes/no): ")
        
    if play_again.lower() == "no":
        break
    
print("\nThank you for playing!\n")
