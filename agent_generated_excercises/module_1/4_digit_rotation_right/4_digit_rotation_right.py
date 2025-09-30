n = int(input())
fd = n // 100
sd = n // 10 % 10
ld = n % 10

print(int(f"{ld}{fd}{sd}"))
print(ld * 100 + fd * 10 + sd)
# Check if there is possibility to solve this with only arithmetic operations, avoid strings