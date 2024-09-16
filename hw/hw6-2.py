# START
from random import randint

random_number: int = randint(1, 100);
tries: int = 0;
user_guess = -1;
while user_guess != random_number:
    user_guess = int(input("guess the number:"))
    tries += 1;
    if user_guess > random_number:
        print("your number is too big")
    elif user_guess < random_number:
        print("your number is too small");
else:
    print("\033BINGO\033[0m")  ## in BOLD
    print(f"you guessed the number in {tries} tries")

# END
