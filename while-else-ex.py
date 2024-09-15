# tries = 0;
# num = -1;
# LUCK_NUMBER: int = 777;
# BREAK_NUMBER = 0;
# while num != LUCK_NUMBER:
#     num: int = int(input("enter number:"));
#     tries += 1;
#     if num == BREAK_NUMBER:
#         print(f"you failed!, you guessed the break number: {num} in {tries} tries")
#         break;
# else:
#     print(f"well done!, you guessed the number {num} in {tries} tries")


N:int=3;sum_n:int=0;
for _ in range(N):
    num: int = int(input("enter number:"));
    if not 0<num<100:
        print("invalid value:",num)
        break;
    sum_n+=num;
else:
    print(f"avg={sum_n//N}")