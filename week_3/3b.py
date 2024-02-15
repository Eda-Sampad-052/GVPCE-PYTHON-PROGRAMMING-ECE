def minput():
    A = []
    a = int(input("Enter the number of rows: "))
    b = int(input("Enter the number of columns: "))
    for i in range(a):
        row = []
        for j in range(b):
            c = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(c)
        A.append(row)
    return A

def mprint(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=" ")
        print()

def madd(A, B):
    C = []
    for i in range(len(A)):
        r = []
        for j in range(len(A[0])):
            r.append(A[i][j] + B[i][j])
        C.append(r)
    mprint(C)

def mtrans(A):
    T = []
    for i in range(len(A[0])):
        r = []
        for j in range(len(A)):
            r.append(A[j][i])
        T.append(r)
    mprint(T)

def mmulti(A, B):
    M = []
    for i in range(len(A)):
        r = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += A[i][k] * B[k][j]
            r.append(s)
        M.append(r)
    mprint(M)

A = minput()
B = minput()

print("\nMatrix 1:")
mprint(A)

print("\nMatrix 2:")
mprint(B)

print("\nMatrix Addition:")
madd(A, B)

print("\nTranspose of Matrix 1:")
mtrans(A)

print("\nTranspose of Matrix 2:")
mtrans(B)

print("\nMatrix Multiplication:")
mmulti(A, B)
