try:
    a=int(input("enter no of fresh loaves="))
    b=int(input("enter no of old loaves="))
    c=a*185
    d=b*185*0.6
    print("the regular price of loves is=185")
    print("amount of new loaves is=",c)
    print("amount of old loaves is=",d)
    print("total amount=",c+d)
except ValueError:
    print("please enter only positive values")
