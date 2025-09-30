h = int(input())
m = int(input())
diff = int(input())

hm_total = (h * 60 + m)
diff_m = diff * 60

hrs = ((hm_total + diff_m) // 60) % 24
mins = ((hm_total + diff_m) % 60)
print(hrs, mins)
