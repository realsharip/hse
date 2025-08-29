n = int(input())
h = (n // 3600) % 24
m = (n // 60) % 60
s = (n % 60)

# Fetching first and last digit for minutes
m1 = m // 10
m2 = m % 10

# Fetching first and last digit for seconds
s1 = s // 10
s2 = s % 10

# Convert into string
mm = f"{m1}{m2}"
ss = f"{s1}{s2}"
print(h, mm, ss, sep=":")
