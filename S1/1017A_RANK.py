# Find the Rank
import array
total = []
def toprank(a, b, c, d):
    sum = 0
    if 0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100 and 0 <= d <= 100:
        sum = a + b + c + d
        total.append(sum)

n = int(input())
if 1 <= n <= 1000:
    for i in range(n):
        a, b, c, d = map(int, input().split())
        toprank(a, b, c, d)
    rank = 1
    for j in range(0, len(total)):
        if total[0] < total[j]:
            rank += 1
    print(rank)
