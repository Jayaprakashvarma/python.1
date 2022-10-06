m=int(input("enter he number of rows m1:"))
n=int(input("enter the number columns in m1:"))
a=[]
for i in range(m):
    b=[]
    for j in range(m):
        c=int(input("enter the numbers of rows in m2:"))
        b.append(c)
     a.append(b)
p=int(input("enter the number of rows in m2:"))
q=int(input("enter the number of column in m2:"))
a1=[]
for i in range(p):
    b1=[]
    for j in range(q):
        c1=int(input("enter the element of matrix2:"))
        b1.append(b1)
     a1.append(b1)   
print("matrix1:")
for i in range(m):
    for j in range(n):
        print(a1[i][j],end=" ")
       print()
if(m!=p or n!=q):
    print("same no.of rows and column can be added")
else:
    d=[]
    for i in range(m):
        d1=[]
        for j in range(n):
            ma=a[i][j]+a1[i][j]
            d1.append(ma)
        d.append(d1)
    print("added matrix:")
    for i in range (m):
        for j in range(n):
            print(d[i][j],end=" ")
         print()
            
     
