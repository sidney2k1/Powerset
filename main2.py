def totalflip(x,y):
    flips=0
    while(x>0 and y>0):
        t1=x&1
        t2=y&1
        if t1!=t2:
            flips+=1
        x>>=1
        y>>=1
    return flips
x=int(input("Enter a number:"))
y=int(input("enter a number"))
print("Total flips needed:",totalflip(x,y))