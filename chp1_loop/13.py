
lst=[]
n=int(input("Enter size of the list : "))
for i in range(n):
    lst.append(i)
print(lst) 

m=int(input("Number in lst of search : "))
for i in lst:
    if i == m: # searching !
        break
print(i,'Present in lst')