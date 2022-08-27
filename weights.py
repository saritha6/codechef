# cook your dish here
def weights(w,x,y,z):
    if(w==x or w==y or w==z):
        return True
    elif(w==x+y or w==y+z or w==x+z):
        return True
    elif(w==x+y+z):
        return True
    else:
        return False
    
t=int(input())
for _ in range(t):
    w,x,y,z=map(int,input().split())
    res=weights(w,x,y,z)
    if(res):
        print("YES")
    else:
        print("NO")
    
    
    
