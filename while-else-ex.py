tries = 0;
num = -1;
LUCK_NUMBER: int = 777;
BREAK_NUMBER = 0;
while num != LUCK_NUMBER:
    num: int = int(input("enter number:"));
    tries += 1;
    if num == BREAK_NUMBER:
        print("num is 0");
        break;
else:
    print(f"well done!, you guessed the number {num} in {tries} tries")
