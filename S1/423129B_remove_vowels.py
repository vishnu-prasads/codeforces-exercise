txt = input()
new = ""
vowels = "aeiou"

for i in range(0,len(txt)):
    if txt[i] not in vowels:
        new = new + txt[i]
print(new)


