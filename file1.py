import datetime
import menu as m
import file2 as f2
import pickle as p
e=datetime.datetime.now()
d=e.strftime("%I:%M:%S %p")
t=e.strftime("%a, %b %d, %Y")
global yy,y,o,uu,u
y="="*80
yy="="*40
o="\n"
uu=" "
u="-"*70
def smenu():
    print(o,"﹏"*9,"\n┃1. Search More"," "*1,"┃","\n┃2. Update"," "*6,"┃","\n┃3. Delete"," "*6,"┃","\n┃4. Go Back"," "*5,"┃",o,"﹋"*9)
    while True:
        ch=input ("Choose Your Option=")
        if ch=="1":
            print (y),sdoa()
        elif ch=="2":
            print (y),f2.udoa()
        elif ch=="3":
            m.delete ()
        elif ch=="4":
            print (y),m.select ()
        else:
            print(y,"\nInvalid Choice. Enter From 1 To 4"), print (y)
def bill():
    cf=open("doc","rb")
    upd={}
    try:
        while True:
            upd=p.load(cf)
            print (yy,"MEDICINE BILL",yy,"\nName-",upd["Name"],uu*30,"Date-",t,d), print ("Address-",upd["Address"]),print ("Phone Number-",upd["Phone Number"]), print (y), print ("SR.NO",uu*2,"MEDICINE NAME",uu*2,"QUANTITY",uu*2,"MRP",uu*2,"TOTAL")
            for i in range(1,10000):
                    upd=p.load(cf)                
                    L2=15-len(upd["Item Name"])
                    L3=10-len(str(upd["Quantity"]))
                    L4=5-len(str(upd["MRP"]))
                    print (upd["Sr.no"],uu*6,upd["Item Name"],uu*L2,upd["Quantity"],uu*L3,upd["MRP"],uu*L4,upd["Total"])
    except EOFError:
                print (o*7)
                print (uu*23,"Including All Taxes")
                print (uu*30,"TOTAL AMOUNT-")
                print (y)
                print (uu*12,"Press Any Key To Continue")
                r=input("-->")
                cf.close()
def sdoa():
	while True:
		ch=input("Want To Search Details (Y/N):")
		if ch=='y' or ch=='Y':
		    	f=False
		    	upd={}
		    	if m.num=="1":
		    	    cf=open('doc', 'rb+')
		    	elif m.num=="2":
		    	    cf=open('dom', 'rb+')
		    	elif m.num=="3":
		    	    cf=open('dos', 'rb+')
		    	elif m.num=="4":
		    	    cf=open('dow', 'rb+')
		    	k=input("\nEnter Name Which You Want To Search:")
		    	try:
		    	    while True:
		    	        rpos = cf.tell()
		    	        upd= p.load(cf)
		    	        if upd["Name"] == k:
		    	            f=True
		    	            print (y),m.pd(upd)
		    	except EOFError:
                                if f==False:
                                    print(y,o,"\nSorry, The Name","\"",k,"\"","Is Not Found In Our Records!","\nPlease Try Again: )\n"),print(y)
                                else:
                                    print("\nSearch Successful."),print(y),smenu()
		elif ch=='n' or ch=='N':
		    print (y),m.select ()
		else:
		    print(y,"\nChoose Correct Option!"),print(y),sdoa()
def adoa():
	while True:
		ch=input("Want To Add Details (Y/N):")
		add={}
		if ch=='y' or ch=='Y':
			if m.num=="1":
			    cf=open("doc","ab")
			    foc=open("doc","ab")
			    name=input("Name of Customer:")
			    age=input("Age:")
			    gender=input("Gender:")
			    address=input("Enter Address:")
			    ph=input("Enter Phone Number:")
			    add["Name"]=name
			    add["Age"]=age
			    add["Gender"]=gender
			    add["Address"]=address
			    add["Phone Number"]=ph
			    add["Date"]=t
			    p.dump(add,cf)
			    cf.flush()
			    print (u)
			    for i in range (1,100):
			        print("\n1. add","\n2. generate bill","\n3. exit")
			        ch=input("-->")
			        if ch=="1":
			            lis={}
			            print (),print (i,"Item-")
			            mname=input ("Item Name:")
			            quantity=int(input ("Quantity:"))
			            MRP=int(input ("MRP:"))
			            Total=quantity*MRP
			            lis["Sr.no"]=i
			            lis["Item Name"]=mname
			            lis["Quantity"]=quantity
			            lis["MRP"]=MRP
			            lis["Total"]=Total
			            p.dump(lis,cf)
			            cf.flush()
			        elif ch=="2":
			            bill()
			        elif ch=="3":
			            break
			elif m.num=="2":
			    cf=open("dom","ab")
			    medicine=input("\nEnter Name Of Medicine:")
			    ca=input("Enter Name Of Company:")
			    manufacturing=input("Enter Date Of Manufacturing:")
			    expire=input("Enter Date Of Expiry:")
			    quantity=input("Enter Quantity:")
			    price=input("Enter Price:")
			    add["Name"]=medicine
			    add["Company Product"]=ca
			    add["Manufacturing"]=manufacturing
			    add["Expiry"]=expire
			    add["Quantity"]=quantity
			    add["Price"]=price
			    p.dump(add,cf),cf.flush(),cf.close()
			elif m.num=="3":
			    cf=open("dos","ab")
			    name=input("\nEnter Name Of Supplier:")
			    age=input("Enter Age:")
			    dos=input("Enter Date Of Supply:")
			    ca=input("Enter Name Of Company:")
			    ta=input("Enter Total Amount:")
			    address=input("Enter Address:")
			    ph=input("Enter Phone Number:")
			    add["Name"]=name
			    add["Age"]=age
			    add["Date Of Supply"]=dos
			    add["Company Product"]=ca
			    add["Total Amount"]=ta
			    add["Address"]=address
			    add["Phone Number"]=ph
			    p.dump(add,cf),cf.flush(),cf.close()
			elif m.num=="4":
			    cf=open("dow","ab")
			    name=input("\nEnter Name Of Worker:")
			    age=input("Enter Age:")
			    doj=input("Enter Date Of Joining:")
			    salary=input("Enter Salary:")
			    address=input("Enter Address:")
			    ph=input("Enter Phone Number:")
			    dol=input("Enter Date Of Leaving:")
			    add["Name"]=name
			    add["Age"]=age
			    add["Date Of Joining"]=doj
			    add["Salary"]=salary
			    add["Address"]=address
			    add["Phone Number"]=ph
			    add["Date Of Leaving"]=dol
			    p.dump(add,cf),cf.flush(),cf.close()
			print("-"*80,"\nDetails Are Added In Record."),print ("-"*80)
		elif ch=="n" or ch=="N":
			print (y),m.select ()
		else:
			print(y,"\nChoose Correct Option!"),print (y),adoa()
def list():
    upd={}
    if m.num=="1":
        cf=open("doc","rb")
        print("Record Is-")
        try:
            while True:
                upd=p.load(cf)
                print(upd)
        except EOFError:
            cf.close(), print (y)
    else:
        if m.num=="2":
            cf=open("dom","rb")
        elif m.num=="3":
            cf=open("dos","rb")
        elif m.num=="4":
            cf=open("dow","rb")
        print("LIST-\n")
        try:
            for i in range(1,10000):
                upd=p.load(cf)
                print (i,"Record Is -"),m.pd(upd)
        except EOFError:
            cf.close(), print (y)