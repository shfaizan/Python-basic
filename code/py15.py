'''find net salary of empolyee net salary =basic salary +da +hra +ma-pf-it
where   da = 70%
        hra = 15%
        ma=rs 1000 fixed
        pf= 8%
        it =12%
'''
bs = int(input("enter basic salary:"))
da = bs*70/100
hra = bs*15/100
ma =1000
pf = bs*8/100
it = bs*12/100

ns = bs + da + hra + ma - pf - it  
print("net salary is ",ns)

print("ID: 17103455 Name : Faizan Shaikh")
