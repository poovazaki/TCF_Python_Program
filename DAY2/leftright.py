n=input("Enter a string:")
count=""
res=""
for i in n:
    if i=='0':
        count=count+i
    else:
       res=res+i
print(res+count)
