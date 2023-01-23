def elections(x):
    if 1 <= x <= 1000000 :
        if x <= 5:
            print("1")
        elif x%5 == 0:
            print((int(x/5)))
        else:
            print((int(x/5))+1)
    else:
        exit()
x = int(input())
elections(x)
