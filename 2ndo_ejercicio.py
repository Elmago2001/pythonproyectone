a=([1,1,1,3,5,1,1,3,3],)
a=a[0]
print(a)
def empaquetar(a):
    lista, n=[],1
    for i in range(0,len(a)-1):
        if a[i]==a[1+i]:
            if i!=len(a)-2:
             n=n+1  
            else:
             n=n+1   
             b=(a[i],n)
             lista.append(b)
        else:
           b=(a[i],n)
           lista.append(b)
        n=1 
    return lista               
print(empaquetar(a))