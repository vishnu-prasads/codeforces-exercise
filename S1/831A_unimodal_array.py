n = int(input())
a = list(map(int,input().split()))

def incr():
    p = 0
    for i in range(1,n):
        if a[i-1] < a[i]:
            p = i
            continue
        else: 
            p = i - 1
            break
    return p
def const():
    q = 0 
    p = incr()
    for i in range(p+1,n):
        if a[i-1] == a[i]:
            q = i
            continue
        else:
            q = i - 1
            break
    return q        
def decr():
    r = 0 
    q = const()
    for i in range(q+1,n):
        if a[i-1] > a[i]:
            r = i
            continue
        else:
            r = i - 1
            break
    return r  


def is_unimodal(n,a):
    if n == 1:
        print("YES")
        exit()
    else:
        p = incr()
        if p == n-1:
            print("YES")
            exit()
        else:
            q = const () 
            if q == n-1:
                print("YES")
                exit()
            else:
                r = decr()
                if r == n-1:
                    print("YES")
                    exit()
                else:
                    print("NO")
                    exit()
is_unimodal(n,a)
