t = int(input())
for i in range(t):
    x,y=map(int,input().split())
    tx = 1*x
    ty = 1*y
    if tx == ty:
        print('ANY')
    if tx > ty:
        print('SECOND')
    if tx < ty:
        print('FIRST')
