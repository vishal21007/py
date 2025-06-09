
'''
write a program to find the first no. in a list that is grat er then ten 
'''

lst=['apple','banana','date','cherry']
print("Values in list",lst)

w_str=input("Enter what do want search in list : ")

flag = 0 # flagging

for char in lst:
    if w_str == char:
        print(w_str,"Present in list")
        flag = 1
        break

if flag == 0:
    print('Value not in list !')