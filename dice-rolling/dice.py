import random 

print("Dice rolling game.")
print("Press enter for play and press q to quite \n")

while True:
    user_input = input("Roll the dice? ")

    if user_input.lower() == 'q':
        print("thanks for playing.")
        break
    
    dice_value = random.randint(1, 6)

    print(f"🎯 You rolled a {dice_value}!\n")