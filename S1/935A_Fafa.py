def employee(n):
    tl = 0
    if 2 <= n <= 100000:
        for i in range(1,n):
            if (n - i) % i == 0:
                tl += 1
        return(tl)
    else:
        exit()
n = int(input())
result = employee(n)
print(result)
        
