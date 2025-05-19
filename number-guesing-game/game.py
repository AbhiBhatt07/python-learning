import random  # import random number.


# make defination of game.
def number_guessing_game():
    number_to_guess = random.randint(
        1, 100
    )  # set vaiable to store randome guessing number
    attempt = 0 # and this if how many time user guess the number. 

    print("🎮 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True: # loop run untill right number is not guess
        try: 
            guess = int(input("Enter you guessing Number: "))
            attempt += 1 
            
            if guess < number_to_guess: 
                print("It's to Low! Try again.")
            elif guess > number_to_guess: 
                print("It's to Hign! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempt} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")
           

# Run the game while calling the function.
number_guessing_game()
            