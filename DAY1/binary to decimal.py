n=input()
res=0
for i in range(len(n)):
    res= res+int(n[i])*(2**(len(n)-1-i))
print(res)
    
