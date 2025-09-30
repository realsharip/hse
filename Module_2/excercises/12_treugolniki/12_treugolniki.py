a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if a >= b and a >= c:
        if a*a == b*b + c*c:
            print("rectangular")
        elif a*a < b*b + c*c:
            print("acute")
        else:
            print("obtuse")
    elif b >= a and b >= c:
        if b*b == a*a + c*c:
            print("rectangular")
        elif b*b < a*a + c*c:
            print("acute")
        else:
            print("obtuse")
    else:
        if c*c == a*a + b*b:
            print("rectangular")
        elif c*c < a*a + b*b:
            print("acute")
        else:
            print("obtuse")
else:
    print("impossible")
