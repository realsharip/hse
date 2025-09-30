n = int(input())
isEven = n % 2 == 0
print(isEven)

s1 = int(input())
n1 = int(input())

s2 = int(input())
n2 = int(input())

# isS1in2 = s2 <= s1 <= n2
# isN1in2 = s2 <= n1 <= n2
#
# isS2in1 = s1 <= s2 <= n1
# isN2in1 = s1 <= n2 <= n1
# ans = isS1in2 or isN1in2 or isS2in1 or isN2in1

ans = s1 <= n2 and s2 <= n1

print(ans)

# start1(3)-------------------------------------------finish1(15)
#         start2(5)----------------------------finish2(10)
