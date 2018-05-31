import cx_Oracle
class staff();
	def staffdetails(self):
	    print("enter the username")
	    self.user1=str(input())
	    print("enter the password")
	    self.pass1=str(input())
	    print("enter the type of vechile you insert y/n")
	    a=="y":
	    	print("enter the car name")
	    	car1=str(input())
	    	print("enter the car cost")
	    	cs=str(input())
	    else:
	    	print("enter the van name")
	    	van1=str(input())
	    	print("enter the van cost")
	    	cs1=str(input())
	    	
	    	
	    
	   
	    con=cx_Oracle.connect("nouffel/nouffel@127.0.0.1/XE")
	    cur=con.cursor()
                sql = "insert into staffdetails VALUES('%s','%s','%s','%s')" % (self.user1,self.pass1,self.car1,self.cs,self.van1,self.cs1)
                cur.execute(sql)
                con.commit()
class account();
	def detils(self):
	    print("enter the first name")
	    self.first=str(input())
	    print("enter the last name")
	    self.last=str(input())
	    print("enter the phone number")
	    self.phone=str(input())
	    print("enter the  password")
	    self.password=str(input())
	    con=cx_Oracle.connect("nouffel/nouffel@127.0.0.1/XE")
	    cur=con.cursor()
                sql = "insert into details VALUES('%s','%s','%s','%s')" % (self.first,self.last,self.phone,self.password)
                cur.execute(sql)
                con.commit()
class van():
	def vandetails(self):
	    global status1
	    print("enter the van vehicle name")
	    self.name1=str(input())
	    print(" ")
	    print("enter the van model name")
	    self.model1=str(input())
	    print(" ")
	    print("enter  van registration number")
	    self.reg1=str(input())
	    print("enter the boarding place")
	    self.bo1=str(input())
	    print("enter the departure place")
	    self.dep1=str(input()) 
	    print("enter the van cost")
	    self.cost1=str(input())
	    print("enter the van fuel consumption")
	    self.fuel1=str(input())
	    print("enter the booking status y/n")
	    st1=str(input())
	    st1.lower()
	    if
			st1=="y":
	    	status1="booked"
	    else:
	    	status="not booked"
	    con=cx_Oracle.connect("nouffel/nouffel@127.0.0.1/XE")
        cur=con.cursor()
        sql = "insert into van VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.name1,self.model1,self.reg1,self.bo1,self.dep1,self.cost1,self.fuel1,status1)
        cur.execute(sql)
        con.commit
class car():
	def cardetails(self):
	    global status
	    print("enter the car vehicle name")
	    self.name=str(input())
	    print(" ")
	    print("enter the car model name")
	    self.model=str(input())
	    print(" ")
	    print("enter the car registration number")
	    self.reg=str(input())
	    print("enter the boarding place")
	    self.bo=str(input())
	    print("enter the departure place")
	    self.dep=str(input())
	    print("enter the car cost")
	    self.cost=str(input())
	    print("enter the car fuel consumption")
	    self.fuel=str(input())
	    print("enter the booking status y/n")
	    st=str(input())
	    st.lower()
	    if st=="y":
	    	status="booked"
	    else:
	    	status="not booked"
        con=cx_Oracle.connect("nouffel/nouffel@127.0.0.1/XE")
        cur=con.cursor()
        sql = "insert into car VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.name,self.model,self.reg,self.bo,self.dep,self.cost,self.fuel,status)
        cur.execute(sql)
        con.commit()
class customer(car,van,details):
   while(1):
   	print(" are a new customer y/n ")
   	if t=="y":
                     dd=account()
                     dd.details()
            else:
                     con=cx_Oracle.connect("nouffel/nouffel@127.0.0.1/XE")
	         cur=con.cursor()
	         print("enter the username")
	         user=str(input())
	         print("enter the password")
	         pa=str(input())
	         sql = "select  from details where uname='%s'" % (user)
	         cur.execute(sql)
	         valu=cur.fetchone()
                     if value is None:
                     print(" ")
                     print("please enter the correct user name")
                     vv=str(input())
	         iu=str(input())
	         iu.lower()
	         if iu=="y":
                        	print("enter the type of vehicle")
   	            	f=str(input())
   	            	f.lower()
   	                        if f=="car":
   		              	d=car()
   		            	d.cardetails()
                     else:
   	             	ff=van()
   	             	ff.vandetails()
   	            	print(" want to book car/van y/n")
	            	t=str(input())
   	            	t.lower()
   	            	ss=staff()
   	            	ss.staffdetails()
   	
   			
