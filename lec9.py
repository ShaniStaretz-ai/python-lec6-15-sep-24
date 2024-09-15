# from random import randint, uniform,choice
#
# # print(randint(0, 3))
# # print(uniform(0, 3))
# print(choice([True,False,"sunday"]))

# for _ in range(5):
#     height: float = float(input("enter number:"));
#     while not 0.4 <= height <= 2.5:
#         height: float = float(input("enter number:"));
#     else:
#         print(height)


# N:int=4
# for _ in range(N):
#     for _ in range(N):
#         print("*",end=" ")
#     print()

n:int=int(input("enter number:"));
for i in range(n+1):
    for _ in range(i):
        print("*",end=" ")
    print()