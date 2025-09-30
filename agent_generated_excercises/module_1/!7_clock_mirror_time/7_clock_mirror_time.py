h = int(input())
m = int(input())

h_reversed = (12 - h) % 12 - 1
m_reversed = (60 - m) % 60

print(h_reversed, m_reversed)