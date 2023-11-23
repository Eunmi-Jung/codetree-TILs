def GCF(a,b):
    if a>b:
        s=a#(다용도 변수)
    else:
        s=b
    for i in range(s-1,0,-1):
        if a%i==0 and b%i==0:
            print(i)
            break
n,m=map(int,input().split())
GCF(n,m)