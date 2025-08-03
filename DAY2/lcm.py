a=int(input())
b=int(input())
res=a*b
small=min(a,b)
for i in range(1,small+1):
    if(a%i==0 and b%i==0):
        gcd=i
print(res/gcd)
