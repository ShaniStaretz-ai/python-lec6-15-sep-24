# START
sum_temperature: int = 0;
for _ in range(5):
    temperature = int(input("enter temperature:"));
    while temperature < -50 or temperature > 45:
        temperature = int(input("try enter a valid temperature:"));
    else:
        sum_temperature += temperature;
print(f"the average of all temp is {sum_temperature // 5}");
# END
