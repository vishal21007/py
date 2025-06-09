print('Enter your destination')
print('press 1 : Domestic')
print('press 2 : International')
ch=input("Enter your choice :")
weight=float(input("Enter weight of the object to be shiped"))

if ch=='1':
    if weight>=0 and weight<1:
        print("Coast for transportation :$5")
    elif weight>=1 and weight<=5:
        print("Coast for transportation :$10")
    elif weight>=5:
        print("Coast for transportation :$15")

elif ch=='2':
    delivery = input("press 1:for standard delivery \npress 2:express delivery :")    
    if weight>=0 and weight<1:
        if delivery == '1':
            print("Coast for transportation :$15")
        else:
            print("For express delivery $25")
    elif weight>=1 and weight<=5:
        if delivery == '1':
            print("Coast for transportation :$30")
        else:
            print("For express delivery $45")
    elif weight>=5:
        print("$55 with express delivery" )
else:
    print('Invalid response!')