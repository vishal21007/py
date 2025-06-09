print("press1 : Areaof square: ")
print("press2 : Area of reatangle : ")
print("press3 : Area of circle :")
ch=input("Enter your choise:")
if ch=='1':
    s=int(input("Enter measures of your side :"))
    Area=s*s
    print("Area of square:",Area)
elif ch=='2':
    l=int(input("Enter measure of your length :"))
    b=int(input("Enter your measures of breath :"))
    Area=l*b
    print("area of rectangle :",Area)
elif ch=='3':
    r=int(input("Enter measure of radius :"))
    Area=3.14*r*r
    print("area of circle :",Area)
else:
    print("Invalid response!")