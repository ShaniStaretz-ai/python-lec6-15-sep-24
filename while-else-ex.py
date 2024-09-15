tries = 0;
num = -1;
LUCK_NUMBER: int = 777;
BREAK_NUMBER = 0;
while num != LUCK_NUMBER:
    num: int = int(input("enter number:"));
    tries += 1;
    if num == BREAK_NUMBER:
        print(f"you failed!, you guessed the break number: {num} in {tries} tries")
        break;
else:
    print(f"well done!, you guessed the number {num} in {tries} tries")
