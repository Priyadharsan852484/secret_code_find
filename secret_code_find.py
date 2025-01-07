s=input().strip()
n=int(input())
l=len(s)
w=[]
for i in range(l//n):
    if i%2==0:
        w.append(s[i*n:i*n+n])
    else:
        b=s[i*n :i*n + n]
        w.append (b[::-1])

for j in range(n):
    for i in w:
        print(i[j],end ="")
    
