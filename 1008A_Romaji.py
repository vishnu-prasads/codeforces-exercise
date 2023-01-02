s = input()
n = len(s)
result = "YES"

def is_vowel(ch):
    vowels='aeiou'
    if ch in vowels:
        return True
    else:
        return False


if s[-1] in 'aeioun':
    for i in range(0,len(s)-1):
        if (s[i] == 'n' ):
            result = "YES"
            continue
        elif (not is_vowel(s[i]) and not is_vowel(s[i+1])):
                result = "NO"
                break

else:
    result = "NO"
    
print (result)