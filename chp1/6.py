#garde calculator write a program that asks the user for a numerical score (0-100)

mark=int(input("enter your marks"))

if mark>90 and mark<100:
    print('Grade A')
elif mark>79 and mark<90:
    print('Grade B')
elif mark>69 and mark<79:
    print('Grade C')
elif mark>59 and mark<69:
    print('Grade D')
elif mark>0 and mark<59:
    print('Grade F')
else:
    print('Invalid Response !')