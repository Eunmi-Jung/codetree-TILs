def s(n):
    for i in range(n):
        for ii in range(n):
            print(i*n+ii+1-(i*n+ii)//9*9,end=" ")
        print()
N=int(input())
s(N)