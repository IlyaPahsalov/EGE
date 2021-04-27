File=open("ex2558.txt")
s=File.readlines()
k=0
for i in s:
    for b in range(2,len(i)):
        if i[b-2]=='A' and i[b]=='R':
            k+=1
            break;
print(k)
