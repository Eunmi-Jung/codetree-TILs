def G(a,b):
    for i in range(1,min(n,m),+1):
        if a%i==0 and b%i==0:
            g=i
    print(g)
n,m=map(int,input().split())
G(n,m)