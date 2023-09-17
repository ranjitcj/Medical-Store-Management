import datetime
import file1 as f1
import file2 as f2
import pickle as p
import os
e=datetime.datetime.now()
d=e.strftime("%I:%M:%S %p")
t=e.strftime("%a, %b %d, %Y")
global y,o,u
y="="*171
o="\n"
u=17
def ex():
    print("\nHold on!","\nAre you sure you want to exit?","\n1.     RESUME","\nEnter. QUIT")
    while True:
        ch=input("-->")
        if ch=="1":
            print(y),menu()
        elif ch=="":
            print(y),exit("See you soon.")
        else:
            print (y,"\nInvalid Choice."),print (y)
    select1()
def med(upd):
    L1=21-len(upd["Name"])
    L2=21-len(upd["Company Product"])
    L3=21-len(upd["Manufacturing"])
    L4=21-len(upd["Expiry"])
    L5=21-len(upd["Quantity"])
    L6=21-len(upd["Price"])
    print(o,"﹏"*26,"\n┃Name Is"," "*15,upd["Name"]," "*L1,"┃","\n┃Company Product Is"," "*4,upd["Company Product"]," "*L2,"┃","\n┃Manufacturing Date Is"," "*1,upd["Manufacturing"]," "*L3,"┃","\n┃Expiry Date Is"," "*8,upd["Expiry"]," "*L4,"┃","\n┃Quantity Is"," "*11,upd["Quantity"]," "*L5,"┃","\n┃Price Is"," "*14,upd["Price"]," "*L6,"┃",o,"﹋"*26)
def sup(upd):
    L1=21-len(upd["Name"])
    L2=21-len(upd["Age"])
    L3=21-len(upd["Date Of Supply"])
    L4=21-len(upd["Company Product"])
    L5=21-len(upd["Total Amount"])
    L6=21-len(upd["Address"])
    L7=21-len(upd["Phone Number"])
    print(o,"﹏"*26,"\n┃Name Is"," "*15,upd["Name"]," "*L1,"┃","\n┃Age Is"," "*16,upd["Age"]," "*L2,"┃","\n┃Date Of Supply Is"," "*5,upd["Date Of Supply"]," "*L3,"┃","\n┃Company Product Is"," "*4,upd["Company Product"]," "*L4,"┃","\n┃Total Amount Is"," "*7,upd["Total Amount"]," "*L5,"┃","\n┃Address Is"," "*12,upd["Address"]," "*L6,"┃","\n┃Phone Number Is"," "*7,upd["Phone Number"]," "*L7,"┃",o,"﹋"*26)
def wor(upd):
    L1=21-len(upd["Name"])
    L2=21-len(upd["Age"])
    L3=21-len(upd["Date Of Joining"])
    L4=21-len(upd["Salary"])
    L5=21-len(upd["Address"])
    L6=21-len(upd["Phone Number"])
    L7=21-len(upd["Date Of Leaving"])
    print(o,"﹏"*26,"\n┃Name Is"," "*15,upd["Name"]," "*L1,"┃","\n┃Age Is"," "*16,upd["Age"]," "*L2,"┃","\n┃Date Of Joining Is"," "*4,upd["Date Of Joining"]," "*L3,"┃","\n┃Salary Is"," "*13,upd["Salary"]," "*L4,"┃","\n┃Address Is"," "*12,upd["Address"]," "*L5,"┃","\n┃Phone Number Is"," "*7,upd["Phone Number"]," "*L6,"┃","\n┃Date Of Leaving Is"," "*4,upd["Date Of Leaving"]," "*L7,"┃",o,"﹋"*26)
def pd(upd):
    if num=="1":
        cus(upd)
    elif num=="2":
        med(upd)
    elif num=="3":
        sup(upd)
    elif num=="4":
        wor(upd)
def select1():
    while True:
        ch=input("Choose Your Option=")
        if ch=="1":
            print(y),f1.adoa(),menu(),print(y)
        elif ch=="2":
            print(y),f1.sdoa(),print(y)
        elif ch=="3":
            print(y),f2.udoa(),print(y)        
        elif ch=="4":
            print(y),delete (), select()
        elif ch=="5":
            print(y),f1.list(),select(),print(y),menu()
        elif ch=="6":
            print(y),menu(),print(y)
        elif ch=="7":
            print(y),ex()
        else:
            print(y,"\nInvalid Choice. Enter From 1 To 7"), print (y)
def delete ():
    if num=="1":
        org=open("doc","rb+")
    elif num=="2":
        org=open("dom","rb+")
    elif num=="3":
        org=open("dos","rb+")
    elif num=="4":
        org=open("dow","rb+")
    temp=open("dioa","ab")
    upd={}
    f=False
    k=input ("\nEnter The Name Which You Want To Delete:")
    try:
        while True:
            upd=p.load(org)
            if upd["Name"]==k:
                f=True
                print (y,o),pd(upd),print("\nAbove Detail Is Successfully Deleted."),print (y)
                continue
                p.dump(upd,org)
                s.clear()
            else:
                p.dump(upd,temp)
    except EOFError:
        org.close(),temp.close()
    if f==False:
        print(y,o,"\nSorry, The Name","\"",k,"\"","Is Not Found In Our Records!","\nPlease Try Again: )\n"),print (y)        
    if num=="1":
        os.remove("doc")
        os.rename("dioa","doc")
    elif num=="2":
        os.remove("dom")
        os.rename("dioa","dom")
    elif num=="3":
        os.remove("dos")
        os.rename("dioa","dos")
    elif num=="4":
        os.remove("dow")
        os.rename("dioa","dow")
def menu():
    print("\nMENU\n","﹏"*17,"\n┃1. Details Of Customers"," "*5,"┃","\n┃2. Details Of Medicines"," "*5,"┃","\n┃3. Details Of Suppliers"," "*5,"┃","\n┃4. Details Of Workers"," "*7,"┃","\n┃5. Exit"," "*21,"┃",o,"﹋"*17)
    global num
    num=input("Want To Know Details Of:-")
    print (y),select ()
def select ():    
    if num=="5":
        ex()    
    elif num=="1":
        a="Customers"
        b="\nCUSTOMERS\n"
    elif num=="2":
        a="Medicines"
        b="\nMEDICINES\n"
    elif num=="3":
        a="Suppliers"
        b="\nSUPPLIERS\n"
    elif num=="4":
        a="Workers  "
        b="\nWORKERS\n"
    else:
        print("Invalid Choice. Enter From 1 To 5"), print (y),menu()
    print(b,"﹏"*20,"\n┃1. Add Details Of New",a," "*3,"┃","\n┃2. Search Details Of",a," "*4,"┃","\n┃3. Update Details Of",a," "*4,"┃","\n┃4. Delete Details Of",a," "*4,"┃","\n┃5. Details Of Old",a," "*7,"┃","\n┃6. Go To Menu"," "*21,"┃","\n┃7. Exit"," "*27,"┃",o,"﹋"*20)
    select1()
print(y*2,o,d,o,t,o*6,"\t"*u,"","﹏"*17,o,"\t"*u,"┃"," "*28,"┃",o,"\t"*u,"┃   WELCOME TO MEDICAL SHOP    ┃",o,"\t"*u,"┃"," "*28,"┃",o,"\t"*u,"","﹋"*17,o*5),print(y*2)
def password():
    k="mry"
    for i in range(3,0,-1):
        l=input("Enter Your Password To Access:")
        if l==k:
            print(y),menu()
        else:
            print(y),print("\t"*3,"Incorrect Password!"),print(y)
    if i==1:
        print("\t"*2,"Too Many Attempts!! Try Again later_/\_"),print(y),exit()
password()