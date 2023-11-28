n=int(input())
cnt=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ord("A")+(cnt-cnt//(ord("Z")-ord("A")))),end="")
        cnt+=1
    print()