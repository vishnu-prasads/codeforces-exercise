#Golden Plate

cells = 0
w, h, k = map(int,input().split())
for i in range (k):
    if 3 <= w <= 100 and 3 <= w <= 100:
        cells += w * 2 + (h -2 ) * 2
        w -= 4
        h -= 4
    else:
        exit()

print(cells)

