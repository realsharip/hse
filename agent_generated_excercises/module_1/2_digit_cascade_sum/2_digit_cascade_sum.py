n = int(input())

fd = n // 100
sd = n // 10 % 10
td = n % 10

print(fd + (fd +sd) + (fd + sd + td))
