n = int(input())
k = 2

while k * k <= n:
    if n % k == 0:
        print(k)
        break
    k += 1
else:
    print(n)
