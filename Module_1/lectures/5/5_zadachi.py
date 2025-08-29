a = int(input())
b = int(input())
c = int(input())
d = int(input())

k_first = a * 100 + b
k_second = c * 100 + d
k_total_price = k_first + k_second
print(k_total_price // 100, k_total_price % 100)

n = int(input())
print(n % 256)