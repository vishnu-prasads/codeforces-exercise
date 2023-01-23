n = int(input())
num = list(map(int,input().split()))
if n - min(num) < max(num) - 1:
    print("black")
elif n - min(num) > max(num) - 1:
    print("white")
else:
    print("white")