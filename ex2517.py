File = open ("ex2517.txt")
s=File.readline()
k=0
lensr=[]
for i in s:
    if i!='C' and  i !='D':
        k += 1
    else:
        lensr.append(k)
        k = 0
print(max(lensr))