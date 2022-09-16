#Calculate area of rectangle,traingle and circle using choice function 
def area(choice):
    if choice==1:
        length=float(input("Enter length:\n"))
        breadth=float(input("Enter breadth:\n"))
        print("Area of Rectangle:",length*breadth)
    elif choice==2:
        base=float(input("Enter base:\n"))
        height=float(input("Enter height:\n"))
        print("Area of triangle:",0.5*base*height)

    elif choice==3:
        radius=float(input("Enter radius:\n"))
        print("Area of circle:",3.14*radius*radius)

print("Enter 1 to Calculate area of rectangle\n Enter 2 to Calculate area of traingle\n Enter 3 to Calculate area of circle\n")

choice=int(input("Enter Choice:"))
area(choice)