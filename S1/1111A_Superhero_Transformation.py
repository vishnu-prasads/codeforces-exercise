s = list(map(str, input().strip()))
t = list(map(str, input().strip()))
if len(s) == len(t):
    for i in range(len(s)): 
        if (s[i] in 'aeiou' and t[i] in 'aeiou') or ( s[i] not in "aeiou" and t[i] not in "aeiou"):
            result = "Yes"
        else:
            result = "No"
            break
    print(result)
else:
    print("No")