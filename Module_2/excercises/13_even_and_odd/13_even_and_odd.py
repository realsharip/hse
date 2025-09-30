a = int(input())
b = int(input())
c = int(input())

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    if (a + b) % 2 != 0 or (a + c) % 2 != 0 or (b + c) % 2 != 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
