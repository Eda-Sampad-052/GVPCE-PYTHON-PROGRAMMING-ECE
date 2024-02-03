a=[0,0,0,0,]
b=[0,0,0,0,]
a[0]=str(input("enter name of student 1: "))
a[1]=int(input("enter age of student 1: "))
a[2]=str(input("enter address of student 1: "))
a[3]=str(input("enter collge of student 1: "))
b[0]=str(input("enter name of student 2: "))
b[1]=int(input("enter age of student 2: "))
b[2]=str(input("enter address of student 2: "))
b[3]=str(input("enter collge of student 2: "))
t1=tuple(a)
t2=tuple(b)
c=()
c=t1+t2
print("concatinated tupled is ",c)