n = int(input())
fruits=list(input().split ())
apples = fruits.count('red')
guava = fruits.count('green')
banana = fruits.count('yellow')
if apples > guava and apples > banana:
 print('apple')
elif guava > apples and guava > banana:
 print('guava')
elif banana > apples and banana > guava:
 print('banana')
else:
 print('none')