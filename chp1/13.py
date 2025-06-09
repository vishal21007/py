s1=int(input("side 1 : "))
s2=int(input("side 2 : "))
s3=int(input("side 3 : "))
if s3==s2==s3:
    print("Equvilateral Triangle")
elif s1==s2 or s2==s3 or s1==s3:
    print("Isoces Triangle") 
else:
    print("scalen Triangle")