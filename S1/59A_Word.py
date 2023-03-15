word = input()
is_upper = 0
is_lower = 0
for i in range(len(word)):
    if word[i].isupper() is True:
        is_upper = is_upper + 1
    else:
        is_lower = is_lower + 1

if is_upper > is_lower:
    print(word.upper())
elif is_upper < is_lower:
    print(word.lower())
else: 
    print(word.lower())

