import random

NUM_SIDES = 6

def main():

    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    total = die1 + die2
    print(f"Dice 1: {die1}, Dice 2: {die2}, Total : {total}")

  
if __name__ == '__main__':
    main()