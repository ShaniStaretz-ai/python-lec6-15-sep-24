# START
n: int = int(input("enter number:"));
str_test: str = ''
if n % 5 == 0:
    str_test += "Fizz"
if n % 3 == 0:
    if str_test:
        str_test += " "
    str_test += "Buzz"
print(str_test)
# END
