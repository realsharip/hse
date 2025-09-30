# i = 1
# while i <= 100:
#     print(i, end=' ')
#     i = i + 1
# print('!')
#
# now = int(input())
# maxNum = now
#
# while now != 0:
#     now = int(input())
#     if now == 0:
#         break
#     if now > maxNum:
#         maxNum = now
# print(maxNum)

# number = 0
#
# while number < 5:
#     print(number)
#     if number == 3:
#         break
#     number = number + 1

# number = 0
#
# while number < 5:
#     print(number)
#     if number == 6:
#         break
#     number = number + 1
# else:
#     print("No longer < 5")

number = 0

while number < 5:
    number = number + 1
    if number == 3:
        continue
    print(number)
else:
    print("No longer < 5")