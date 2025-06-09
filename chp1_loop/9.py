# ask user for a number, sq number from 1 to n. Add all sq number into a list - Lst=[] and print value of list.

lst=[]
squ=int(input("Enter a number : "))
sum=0
for i in range(1,squ+1):
    lst.append(i**2)
    sum=(i**2) + sum
print('Updated values in the list : ',lst,'\nAverage of the list :',sum/squ)





'''sum=0
for var in lst:
    sum=var+sum
print('your sum is :',sum)'''

'''
for i in lst:
    print(i)'''