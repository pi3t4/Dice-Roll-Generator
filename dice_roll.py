import random
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def roll_dice(num_dice):
    print("Rolling the dice...")
    total = 0
    for i in range(num_dice):
        roll_result = random.randint(1, 6)
        print(f'Dice {i + 1}: {roll_result}')
        total += roll_result
    print(f'Total: {total}')

def dice_roll_generator():
    while True:
        clear_screen()
        print("Welcome to the Dice Roll Generator!")
        
        try:
            num_dice = int(input("Enter the number of dice to roll (1 or 2): "))
            if num_dice not in [1, 2]:
                raise ValueError("Please enter a valid number (1 or 2).")
        except ValueError as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")
            continue

        roll_dice(num_dice)

        roll_again = input("Roll again? (y/n): ").lower()
        if roll_again != 'y':
            clear_screen()
            print("Thanks for using the Dice Roll Generator. Goodbye!")
            break

if __name__ == "__main__":
    dice_roll_generator()
