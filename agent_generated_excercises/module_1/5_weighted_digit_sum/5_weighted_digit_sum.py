n = int(input())
fd = n // 100
sd = n // 10 % 10
ld = n % 10

print(4 * fd + 2 * sd + ld)