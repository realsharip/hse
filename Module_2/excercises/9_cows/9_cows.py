n = int(input())

if n % 10 == 1 and n != 11:
    print(n, "korova")

elif n // 10 != 1 and 1 < n % 10 < 5:
    print(n, "korovy")
else:
    print(n, "korov")
