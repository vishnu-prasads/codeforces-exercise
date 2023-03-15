n = int(input())
s = list(map(str, input().strip()))
t = list(s)
t.sort()

if s.count(s[0]) != len(s):
    for i in range(len(s) -1):
        if s[i] > s[i+1]:
            s.remove(s[i])
            print(*s, sep="")
            exit()
if s.count(s[0]) == len(s) and len(s) != 1:
    s.remove(s[0])
    print(*s, sep="")
    exit()
if s == t:
    s.remove(s[-1])
    print(*s, sep="")
    exit()

