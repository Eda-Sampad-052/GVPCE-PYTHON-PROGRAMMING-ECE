a=[]
b=0
for i in range (20,50):
    b=0
    for j in range (2,i):
        if i%j==0:
            b+=1
        else:
            continue
    if b==0:
        a.append(i)
print("the prime numbers from 20 to 50 are ",a)