'''ask cumtomer purchase amount and p amount c type
 a stor offr disco based on cm tpy/reg/mem
 cus=reg
    p_amt=50 - 100,dis=5% of p_amt
    p_amt=over100,dis=10& of p_amt
    less then50=no dis
cus=mem
    p_amt=50 - 100,dis=10% of p_amt
    puramt = over100,dis=20%
    p_amt less then 50=dis5%
calculate final price with dis     
    '''
cus=input("enter customer type Regular/Member: ")
p_amt=int(input("enter your purchase amount : "))
t_amt = 0
if cus=='Regular':
    if p_amt>=0 and p_amt<=50:
        t_amt= p_amt
    elif p_amt>=50 and p_amt<=100:
        d_amt = p_amt * 0.05
        t_amt = p_amt-d_amt
    elif p_amt >100:
        d_amt = p_amt * 0.1
        t_amt = p_amt - d_amt
else:
    if p_amt>=0 and p_amt<=50:
        d_amt= p_amt * 0.05
        t_amt= p_amt - d_amt
    elif p_amt>=50 and p_amt<=100:
        d_amt = p_amt * 0.1
        t_amt = p_amt-d_amt
    elif p_amt >100:
        d_amt = p_amt * 0.2
        t_amt = p_amt - d_amt
print("this is your purchase amount after discount:",t_amt)