import math as m
n=int(input("enter a number : "))
temp=n
sum=0
length=len(str(n))
while(n>0):
    x=n%10
    sum=sum+m.pow(x,length)
    n=n//10
if(sum==temp):
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
