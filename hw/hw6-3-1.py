# START
n: int = int(input("enter number:"))
while n < 0:
    print("invalid number, needs to be bigger than 0")
    n: int = int(input("enter number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# END
