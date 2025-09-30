n = int(input())
m = int(input())
k = int(input())

if (n * m - (n * m - k)) % k == 0:
    print("YES")
else:
    print("NO")