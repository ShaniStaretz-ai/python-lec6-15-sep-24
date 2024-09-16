# START
n = int(input("enter stars number bigger than 0:"))
for i in range(1, n + 2, 2):
    print(f"{('*' * i):^{n}}")
# END
