import menu as m
import pickle as p
global y,o
y="="*80
o="\n"
def udoa():
	while True:
		ch=input("Want To Update Details (Y/N):")
		if ch=='y' or ch=='Y':
		    	upd={}
		    	if m.num=="1":
		    	    cf=open('doc', 'rb+')
		    	elif m.num=="2":
		    	    cf=open('dom', 'rb+')
		    	elif m.num=="3":
		    	    cf=open('dos', 'rb+')
		    	elif m.num=="4":
		    	    cf=open('dow', 'rb+')
		    	k=input("\nEnter Name Which You Want To Update:")
		    	try:
		    	    while True:
		    	        rpos = cf.tell()
		    	        upd= p.load(cf)
		    	        if upd["Name"] == k:
		    	            print(y,o,"\nCurrent Details are-"),m.pd(upd)
		    	            if m.num=="1":
		    	                 print("\nEdit Details of:\n","▁"*20,"\n┃1. Name"," "*14,"┃","\n┃2. Age"," "*15,"┃","\n┃3. Gender"," "*12,"┃","\n┃4. Date"," "*14,"┃","\n┃5. Items list"," "*8,"┃","\n┃6. Total Amount"," "*6,"┃","\n┃7. Delete"," "*12,"┃","\n┃8. Go back"," "*11,"┃",o,"▔"*20)
		    	                 while True:
		    	                    ch=input("Enter The Number You Want To Edit:")
		    	                    if ch=="1":
		    	                        upd["Name"]=input("Enter New Name:")
		    	                    elif ch=="2":
		    	                        upd["Age"]=input("Age:")
		    	                    elif ch=="3":
		    	                        upd["Gender"]=input("Gender:")
		    	                    elif ch=="4":
		    	                        upd["Date"]=input("Enter New Date:")
		    	                    elif ch=="5":
		    	                        upd["Items list"]=input("Enter New list of Items:")
		    	                    elif ch=="6":
		    	                        upd["Total amount"]=input("Enter New Amount:")
		    	                    elif ch=="7":
		    	                        m.delete(),udoa()
		    	                    elif ch=="8":
		    	                        cf.flush()
		    	                        print (y,"\nFinal Updates Are:-"),m.cus(upd),print(y), udoa()
		    	                    else:
		    	                        print(y,"\nChoose Correct Option!"),print(y)
		    	                        continue
		    	                    cf.seek (rpos)
		    	                    cf.flush()
		    	                    p.dump(upd,cf)
		    	                    print ("-"*80),m.cus(upd),print("\nRecord Successfully Updated."),print ("-"*80)
		    	            elif m.num=="2":
		    	               print ("\nEdit Details of:\n","﹏"*13,"\n┃1. Name"," "*14,"┃","\n┃2. Company Product"," "*3,"┃","\n┃3. Manufacturing Date  ┃","\n┃4. Expiry Date"," "*7,"┃","\n┃5. Quantity"," "*10,"┃","\n┃6. Price"," "*13,"┃","\n┃7. Delete"," "*12,"┃","\n┃8. Go back"," "*11,"┃",o,"﹋"*13)
		    	               while True:
		    	                    ch=input("Enter The Number You Want To Edit:")
		    	                    if ch=="1":
		    	                        upd["Name"]=input("Enter New Name Of Medicine:")
		    	                    elif ch=="2":
		    	                        upd["Company Product"]=input("Enter Name Of Company:")
		    	                    elif ch=="3":
		    	                        upd["Manufacturing"]=input("Enter New Date Of Manufacturing Of Medicine:")
		    	                    elif ch=="4":
		    	                        upd["Expiry"]=input("Enter New Date Of Expiry Of Medicine:")
		    	                    elif ch=="5":
		    	                        upd["Quantity"]=input("Enter New Quantity Of Medicine:")
		    	                    elif ch=="6":
		    	                        upd["Price"]=input("Enter New Price Of Medicine:")
		    	                    elif ch=="7":
		    	                       m.delete(),udoa()
		    	                    elif ch=="8":
		    	                        cf.flush()
		    	                        print (y,"\nFinal Updates Are:-"),m.med(upd),print(y), udoa()
		    	                    else:
		    	                        print(y,"\nChoose Correct Option!"),print (y)
		    	                        continue
		    	                    cf.seek (rpos)
		    	                    cf.flush()
		    	                    p.dump(upd,cf)
		    	                    print ("-"*80),m.med(upd),print("\nRecord Successfully Updated."),print ("-"*80)
		    	            elif m.num=="3":
		    	                print ("\nEdit Details of:\n","﹏"*25,"\n┃1. Name"," "*14,"┃","\n┃2. Age"," "*15,"┃","\n┃3. Date Of Supply"," "*4,"┃","\n┃4. Company Product"," "*3,"┃","\n┃5. Total Amount"," "*6,"┃","\n┃6. Address"," "*11,"┃","\n┃7. Phone Number"," "*6,"┃","\n┃8. Delete"," "*12,"┃","\n┃9. Go back"," "*11,"┃",o,""*20)
		    	                while True:
		    	                    ch=input("Enter The Number You Want To Edit:")
		    	                    if ch=="1":
		    	                        upd["Name"]=input("Enter Name:")
		    	                    elif ch=="2":
		    	                        upd["Age"]=input("Enter Age:")
		    	                    elif ch=="3":
		    	                        upd["Date Of Supply"]=input("Enter Date Of supply:")
		    	                    elif ch=="4":
		    	                        upd["Company Product"]=input("Enter Name Of Company:")
		    	                    elif ch=="5":
		    	                        upd["Total Amount"]=input("Enter Total Amount:")
		    	                    elif ch=="6":
		    	                        upd["Address"]=input("Enter Address:")
		    	                    elif ch=="7":
		    	                        upd["Phone Number"]=input("Enter Phone Number:")
		    	                    elif ch=="8":
		    	                        m.delete(),udoa()
		    	                    elif ch=="9":
		    	                        cf.flush()
		    	                        print (y,"\nFinal Updates Are:-"),m.sup(upd),print(y),udoa()
		    	                    else:
		    	                        print(y,"\nChoose Correct Option!"),print (y)
		    	                        continue  		    	                
		    	                    cf.seek (rpos)
		    	                    cf.flush()
		    	                    p.dump(upd,cf)
		    	                    print ("-"*80),m.sup(upd),print("\nRecord Successfully Updated."),print ("-"*80)
		    	            elif m.num=="4":
		    	                print ("\nEdit Details of:\n","▁"*20,"\n┃1. Name"," "*14,"┃","\n┃2. Age"," "*15,"┃","\n┃3. Date Of Joining"," "*3,"┃","\n┃4. Salary"," "*12,"┃","\n┃5. Address"," "*11,"┃","\n┃6. Phone Number"," "*6,"┃","\n┃7. Date of Leaving"," "*3,"┃","\n┃8. Delete"," "*12,"┃","\n┃9. Go back"," "*11,"┃",o,"▔"*20)
		    	                while True:
		    	                    ch=input("Enter The Number You Want To Edit:")
		    	                    if ch=="1":
		    	                        upd["Name"]=input("Enter Name:")
		    	                    elif ch=="2":
		    	                        upd["Age"]=input("Enter Age:")
		    	                    elif ch=="3":
		    	                        upd["Date Of Joining"]=input("Enter Date Of Joining:")
		    	                    elif ch=="4":
		    	                        upd["Salary"]=input("Enter Salary:")
		    	                    elif ch=="5":
		    	                        upd["Address"]=input("Enter Address:")
		    	                    elif ch=="6":
		    	                        upd["Phone Number"]=input("Enter Phone Number:")
		    	                    elif ch=="7":
		    	                        upd["Date Of Leaving"]=input("Enter Date Of Leaving:")
		    	                    elif ch=="8":
		    	                        m.delete(),udoa()
		    	                    elif ch=="9":
		    	                        cf.flush()
		    	                        print (y,"\nFinal Updates Are:-"),m.wor(upd),print(y), udoa()
		    	                    else:
		    	                        print(y,"\nChoose Correct Option!"),print (y)
		    	                        continue
		    	                    cf.seek (rpos)
		    	                    cf.flush()
		    	                    p.dump(upd,cf)
		    	                    print ("-"*80),m.wor(upd),print("\nRecord Successfully Updated."),print ("-"*80)
		    	except EOFError:
		    	    print(y,o,"\nSorry, The Name","\"",k,"\"","Is Not Found In Our Records!","\nPlease Try Again: )\n"),print (y),udoa()
		    	    cf.close()
		elif ch=="n" or ch=="N":
			print (y),m.select()
		else:
			print(y,"\nChoose Correct Option!"),print(y),udoa()