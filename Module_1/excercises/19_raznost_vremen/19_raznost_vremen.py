h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

# Convert into seconds. The same we need to do for h2, m2, s2
h1_sec = h1 % 24 * 3600
m1_sec = m1 % 60 * 60
s1_sec = s1 % 60

h2_sec = h2 % 24 * 3600
m2_sec = m2 % 60 * 60
s2_sec = s2 % 60

# Final print
print((h2_sec + m2_sec + s2_sec) - (h1_sec + m1_sec + s1_sec))
