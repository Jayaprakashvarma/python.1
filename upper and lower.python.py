m=int(input("enter lower"))
n=int(input("enter upper range"))
a=[]
a=[x for x in range(1,n+1)
   if(int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)

      
