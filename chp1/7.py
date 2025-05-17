'''body mass index(BMI) catagory: write aprogramthat asks the user for their BMI (body mass index) and print 
their weight category :
BMI less that 18.5:"underweight"
between18.5 -24.9=normal
between25 - 29.9=over
grater then30=obese 
'''
BMI=float(input("enter your BMI "))
if BMI>0 and BMI<=18.5:
    print("underweight")
elif BMI>=18.4 and BMI<=24.9:
    print("Normal weight")
elif BMI>=25 and BMI<29.9:
    print("over weight")
elif BMI>30:
    print("obese")
else:
    print("invalid Response ! ")