#To check  greater number between five numbers 

#take input from user
a=int(input("Enter a\n"))
b=int(input("Enter b\n"))
c=int(input("Enter c\n"))
d=int(input("Enter d\n"))

#using ladder if else conditions
if a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>d:
    print("b is greater")
elif c>d:
    print("c is greater")
else:
    print("d id greater")