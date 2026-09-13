n=int(input("enter your number:"))
if n%2==0:
    print("even")
elif n%2!=0:
    print("odd")
if n<=1:
    print("not prime")
elif n==2 or n==3 or n==5:
    print("prime")
elif n%2==0 or n%3==0 or n%5==0:
    print("not prime")