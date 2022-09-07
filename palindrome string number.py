print("Case 1:Given string is palindrome or not")
print("Case 2:Given number is palindrome or not")
a=int(input(" Case = "))
if(a==1):
    str=input("Enter a string:")
    if(str==str[::-1]):
        print("palindrome")
    else:
        print("Not a palindrome")
else:
    n=int(input("Enter a number:"))
    temp=n
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if(temp==rev):
        print("palindrome")
    else:
        print("not a palindrome")
