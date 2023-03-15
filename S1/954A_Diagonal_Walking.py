n = int(input())
sequence  = input()
#ru_sequence = sequence.replace("RU","D")
#ur_sequence = ru_sequence.replace("UR","D")
#print(len(ur_sequence))
i = 0
result = n
while i < len(sequence) - 1:
    if sequence[i] == "R" and sequence[i+1] == "U":
        result -= 1
        i = i + 2
    elif sequence[i] == "U" and sequence[i+1] == "R":
        result -= 1
        i = i + 2
    else:
        i = i + 1

print(result)
