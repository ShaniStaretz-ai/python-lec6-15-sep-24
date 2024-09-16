# START
count: int = 0;
number: int = int(input("enter number divided by 7:"));
while number % 7 == 0:
    if number % 11 == 0:
        break;
    count += 1;
    number = int(input("enter number divided by 7:"));
else:
    print("counter:", count)

# END
