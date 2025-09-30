n = int(input())
fd = n // 1000
sd = n // 100 % 10
td = n // 10 % 10
ld = n % 10

print(fd * td - sd * ld)