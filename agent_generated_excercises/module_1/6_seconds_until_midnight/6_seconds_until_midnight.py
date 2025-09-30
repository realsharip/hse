h = int(input())
m = int(input())
s = int(input())

s_till_midnight = (24 * 3600 - (h % 24 * 3600 + m % 60 * 60 + s % 60))
print(s_till_midnight)
