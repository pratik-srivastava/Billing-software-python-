from datetime import date
from datetime import time
today=date.today()
a=int(input("Enter the Bill No.__"))
cust_name=input("Enter the Customer's Name:- ")
name=input("Enter the name of the item:- ")
price=float(input("Enter the price of the item:- "))
qty=int(input("Enter the quantity of item:- "))
cg=float(((price/100)*9))
sg=float(((price/100)*9))
pay=float(qty*price)
dis=int(((10/100)*pay))
net=float(pay-dis)

total=float(net+sg+cg)
print("")
print("")
print("")
print("")



print("------------------------------------------------------------")

print("                      Pratik's Cafe                      ")
print("                     Sant Vinoba Marg                    ")
print("                New Colony,Deoria(UP)-274001             ")
print("                  Ph:6388966308,8303295402               ")








print("-----------------------Tax Invoice---------------------------")
print("       Date: ",today,"                   Bill No.  :",a)
print("       PBoy: COUNTER")
print("-------------------------------------------------------------")
print(" Particulars","\t\t\t\t  ","Qty","\t","Rate","\t","Amount")
print("-------------------------------------------------------------")
print(name,"\t\t\t\t     ","    ",qty," \t",round(price,2),"\t",round(pay,2))
print("                                    -------------------------")
print("                         Sub Total:","                   ",round(pay,2))
print("                         Dis: @10%:","                   ",dis)
print("                                    -------------------------")
print("                         Net Total:","                   ",round(net,2))
print("                         CGST: @9%:","                   ",round(cg,2))
print("                         SGST: @9%:","                   ",round(sg,2))
print("-------------------------------------------------------------")
print("                 Grand Total:","                   ",round(total,2))
print("")
print("")
print("GST NO 27AADFH5037M1Z6")
print("E.&0.E.         Thank You      Visit Again    Have a good day")
print("\n")
print("Take Away your order Mr./Mrs.",cust_name)
