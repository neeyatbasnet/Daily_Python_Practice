import random
customers={1:{"name":"Neeyat","Acc_no":123456789,"password":123,"A_bal":549000,"History":[]},
           2:{"name":"Anmol","Acc_no":234567891,"password":234,"A_bal":490005,"History":[]}}

def Registration():
    id=int(input("Enter new id:"))
    if id in customers:
        print("You have already registered . Login to use the services")
        return None
    n=input("Enter your name:")
    while(True):
        p=input("Set a password:")
        p1=input("Confirm new password:")
        if p==p1:
            print("Registered Successfully")
            break
        print("Different passwords.Enter passwords again")
    acc_no=random.randint(100000000,999999999)
    customers[id]={"name":n,"Acc_no":acc_no,"password":p,"A_bal":0}

def Login():
    global cust_id
    cust_id=int(input("Enter cust id:"))
    pswd=int(input("Enter password:"))
    if cust_id in customers:
        if customers[cust_id]["password"]==pswd:
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("Invalid customer id")

def ViewAccountDetails(cust_id):
    print("Customer Details are as:")
    det=customers[cust_id]
    print("Customer id:",cust_id)
    for k,v in det.items():
        print(k,':',v)

def FundTransfer(cust_id):
    an=int(input("Enter the receivers acc no:"))
    amt=int(input("Enter the amount:"))
    x=customers[cust_id]["A_bal"]
    tcid=0
    if x>=amt:
        rem_bal=x-amt
        customers[cust_id]["A_bal"]=rem_bal
        customers[cust_id]["History"].append(f"Amount {amt} debited and credited to Account no {an}")
        for k in customers:
            if customers[k]["Acc_no"]==an:
                tcid=k
    else:
        print("Insufficient Balance")
    
    if tcid!=0:
        customers[tcid]["A_bal"]+=amt
        print("Amount Transferred Successfully")
        customers[tcid]["History"].append(f"Amount {amt} credited")
    print(customers)
    
def ViewTransactionHistory(cust_id):
    for i in customers[cust_id]["History"]:
        print(i)
    


Login()
FundTransfer(cust_id)
ViewTransactionHistory(cust_id)
# ViewAccountDetails(cust_id)
# Registration()
# print(customers)
    
    
