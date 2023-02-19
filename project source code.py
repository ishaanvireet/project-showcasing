import os
import sys
import mysql.connector
import datetime 
now= datetime.datetime.now()
def login():
    print(now)
    ''' to login into the system'''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    print(40*"**","\n\n")
    e=input("enter your user id:")
    sql="SELECT count(*) FROM user where uid=%s;"
    val=(e,)
    cursor.execute(sql,val)
    for i in cursor:
        x=i[0]
    if x==0:
        print("non existent userid")
        login()
    else:
        pw=input("enter your password")
        sql=" SELECT count(*) from user where uid=%s and upwd=%s ;"
        val=(e,pw)
        cursor.execute(sql,val)
        for i in cursor:
            cnt=i[0]
        if cnt!=0:
            print("YOU HAVE LOGED IN SUCCESSFULLY")
            return
        else:
            print("INVALID PASSWORD")
            login()

            
def db_mgmt():
    ''' to manage database'''
    while True:
        print("1.Database creation")
        print("2.List database")
        print("3.back(main menu)")
        p=int(input("Enter Your Choice:"))
        if p==1:
            create_database()
        if p==2:
            list_database()
        if p==3:
            break

def sales_mgmt():
    ''' to manage sales'''
    while True:
        print("1. Sales items")
        print("2. List sales")
        print("3. back(main menu)")
        s=int(input(" Enter your choice :"))
        if s==1:
            manage_sales()
        if s==2:
            list_sale()
        if s==3:
            break
        
def product_mgmt():
    
    ''' to manage products'''
    while True:
       print("1.Add New Product")
       print("2.List Product")
       print("3.Update Product")
       print("4.Delete Product")
       print("5.Back(Main Menu)")
       p=int(input("Enter your choice:"))
       if p==1:
           add_product()
       if p==2:
           search_product()
       if p==3:
           update_product()
       if p==4:
           delete_product()
       if p==5:
          break
        
def mbr_ship():
    ''' to manage prime members'''
    print("Be a member of our store and earn benefits")
    while True:
        print("\t1. Add a member")
        print("\t2.Show details of existing member")
        print("\t3. Back")
        ch=int(input("enter your choice"))
        if ch==1:
            add_mbr()
        if ch==2:
            list_mbr()
        if ch==3:
            break
        
def user_mgmt():
    ''' to manage user'''
    while True:
        print(" 1.Add user")
        print(" 2.List user")
        print(" 3.back (Main Menu)")
        u =int(input("Enter your choice:"))
        if u==1:
            add_user()
        if u==2:
            list_user()
        if u==3:
            break
def ana_lys():
    ''' to produce end of sales analysis'''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    print("Hey, here is your today's summary of the sales")
    sum=0
    sql="SELECT * from sales where salesdate =%s"
    val=(str(datetime.date.today()),)
    cursor.execute(sql,val)
    print("\t\tSales details for the day")
         
    print("-"*80)
    print("salesid\t Date\t Productcode \tprice \tquantity\t total")
    print("-"*80)
    for i in cursor:
        print(i[0],i[1],i[2],i[3],i[4],i[5],sep="\t")
    print("-"*80)
    print(" And here's the report for products stock left less than 50 pcs")
    cursor.execute("SELECT * from product where pqty<=50")
    for i in cursor:
        for x in i:
            print(x,end="\t")
        print()
        
def create_database():
    ''' creating the database'''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    print(" CREATING PRODUCT TABLE")
    sql="CREATE TABLE if not exists product(\
pcode int(4) PRIMARY KEY,\
pname char(30) NOT NULL,\
pprice float(8,2),\
pqty int(4),\
pcat char(30));"
    cursor.execute(sql)
    print("PRODUCT table created")
    print("CREATING MEMBER TABLE")
    sql="CREATE TABLE if not exists mbr(\
mbrid int(4) PRIMARY KEY,\
mname char(50) NOT NULL,\
checkben int(5),\
mcat char(30));"
    cursor.execute(sql)
    print("MEMBER table created")
    print("CREATING SALES TABLE")
    sql="CREATE TABLE if not exists sales(\
salesid int(4) PRIMARY KEY,\
salesdate DATE,\
pcode char(30) NOT NULL,\
pprice float(8,2),\
pqty int(4),\
Total double(8,2));"
    cursor.execute(sql)
    print("SALES table created")
    print("CREATING USERS TABLE")
    sql="CREATE TABLE if not exists user(\
uid char(30) PRIMARY KEY,\
uname char(30) NOT NULL,\
upwd char(30));"
    cursor.execute(sql)
    print("USER table created")


def list_database():
    ''' list the database'''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    sql="show tables;"
    cursor.execute(sql)
    for i in cursor:
        print(i,end="\t\n")
       
def add_user():
    ''' add a user'''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    uid=input("Enter user id:")
    name=input("Enter Name:")
    passwd=input("Enter Password:")
    sql="INSERT INTO user values(%s,%s,%s);"
    val=(uid,name,passwd)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount,"user created")

def list_user():
    ''' lists the users'''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    sql="SELECT * from user;"
    cursor.execute(sql)
    clrscr()
    print("USER DETAILS")
    print("\t\t","-"*40)
    print("\t\t USERID      \t\t\tName\t\tUser_password")
    print("\t\t","-"*40)
    for i in cursor:
        print("\t\t",i[0],"\t\t",i[1],"\t\t",i[2])
    print("\t\t","-"*40)

def manage_sales():
    '''to interactively manage the sales'''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    ch=input("Does customer have membership?----Yes/No")
    if ch.upper()=="YES":
        mbrcode=int(input("enter the member code"))
        sql="SELECT mcat,checkben,mname from mbr where mbrid=%s;"
        v=(mbrcode,)
        cursor.execute(sql,v)
        for i in cursor:
            cat=i[0]
            annre=i[1]
            n=i[2]
        print("\t",n)
        print("\t A",cat," member!!")
        if annre%10==0 and annre!=0:
            print("Time to renew membership before continuing")
            if cat.upper()=="GOLD":
                print("\tCollect Rs 1000 ")
            if cat.lower()=="SILVER":
                print("\tCollect Rs 500")
        if cat.upper()=="GOLD":
            Gtotal=bill_sys()
            print("Customer eligible for 10% discount")
            Gtotal-=Gtotal*0.1
            sql="UPDATE mbr SET checkben=checkben+1 where mbrid=%s"
            val=(mbrcode,)
            cursor.execute(sql,val)
            mydb.commit()
            print("Member details have been updated")
            print("Collect Rs. ",Gtotal,"from the customer")
        else:
            Gtotal=bill_sys()
            print("Customer eligible for 5% discount")
            Gtotal-=Gtotal*0.05
            sql="UPDATE mbr SET checkben=checkben+1 where mbrid=%s"
            val=(mbrcode,)
            cursor.execute(sql,val)
            mydb.commit()
            print("Member details have been updated")
            print("Collect Rs. ",Gtotal,"from the customer")
    else:
        print("Become a member and get esteemed benefits from our store!!")
        Gtotal=bill_sys()
        print("Collect Rs. ",Gtotal,"from the customer")
        
def bill_sys():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    sql="SELECT * from product"
    cursor.execute(sql)
    clrscr()
    print("PRODUCTS AVAILABLE")
    print("\t\t","-"*47)
    print("\tcode \t name\t\t price\t quantity\t category")
    print("\t\t","-"*47)
    for i in cursor:
        print("\t",i[0],"\t",i[1],"\t\t",i[2],"\t",i[3],"\t",i[4])
        print("\t\t","-"*47)
    '''to generate the bill'''
    L=[]
    flag=True
    while flag:
        temp=sale_product()
        if temp!=None:
            L.append(temp)
        ch=input("Customer wants to continue shopping?--Yes/No")
        if ch.upper()=="NO":
            flag=False
            GT=0
            print("Here is the sales summary")
            print("pcode  pprice  quantity  Total")
            for i in L:
                print(i[0]," " ,i[1]," ",i[2],"  ", i[3])
                GT+=int(i[3])
            print("\t Grand Total is:",GT)
            return GT
    
def sale_product():
    ''' to sale a particular item '''
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    pcode=input("enter the product code: ")
    sql="SELECT count(*) from product where pcode=%s;"
    val=(pcode,)
    cursor.execute(sql,val)
    for x in cursor:
        cnt=x[0]
    if cnt !=0:
        cursor.execute("SELECT count(*) FROM sales;")
        for i in cursor:
            a=i[0]
        sql="SELECT * from product where pcode=%s;"
        val=(pcode,)
        cursor.execute(sql,val)
        for x in cursor:
            print(x)
            price=int(x[2])
            pqty=int(x[3])
        qty=int(input("enter no. of quantity : "))
        if qty<=pqty:
            total=qty*price
            sql="INSERT into sales value(%s,%s,%s,%s,%s,%s)"
            val=(int(a)+2,datetime.datetime.now(),pcode,price,qty,total)
            cursor.execute(sql,val)
            sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
            val=(qty,pcode)
            cursor.execute(sql,val)
            mydb.commit()
            return [pcode,price,qty,total]
        else:
            print("quantity not available")
            return
    else:
        print("product is not available")
        return
            
def list_sale():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    sql="SELECT * from sales"
    cursor.execute(sql)
    print("\t\tSales details")
    print("-"*80)
    print("salesid\t Date\t Productcode \tprice \tquantity\t total")
    print("-"*80)
    for i in cursor:
        print(i[0],i[1],i[2],i[3],i[4],i[5],sep="\t")
    print("-"*80)

def add_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    cursor.execute("SELECT count(*) FROM product")
    for i in cursor:
        x=i[0]
    sql="INSERT INTO product values(%s,%s,%s,%s,%s);"
    code=1000+(x+1)
    name=input("Enter product name:")
    qty=int(input("Enter product quantity:"))
    price=float(input("Enter product unit price:"))
    cat=input("Enter Product category:")
    val=(code,name,price,qty,cat,)
    cursor.execute(sql,val)
    mydb.commit()
        
def update_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    code=int(input("Enter the product code:"))
    qty=int(input("Enter the quantity:"))
    sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
    val=(qty,code)
    cursor.execute(sql,val)
    mydb.commit()
    print("Product details updated")
    
def delete_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    code=int(input("Enter the product code:"))
    sql="DELETE FROM product WHERE pcode=%s;"
    val=(code,)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount,"record(s) deleted")
    
def search_product():
    while True:
        print("1.List all product")
        print("2.List product code wise")
        print("3.List product category wise")
        print("4.Back(Main Menu)")
        s=int(input("Enter your choice:"))
        if s==1:
            list_product()
        if s==2:
            code=int(input("Enter product code:"))
            list_prcode(code)
        if s==3:
            cat=input("Enter category:")
            list_prcat(cat)
        if s==4:
            break
        
def list_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    sql="SELECT * from product"
    cursor.execute(sql)
    clrscr()
    print("PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\tcode \t name\t\t price\t quantity\t category")
    print("\t\t","-"*47)
    for i in cursor:
        print("\t",i[0],"\t",i[1],"\t\t",i[2],"\t",i[3],"\t",i[4])
        print("\t\t","-"*47)
        
def list_prcode(code):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    sql="SELECT * from product where pcode=%s"
    val=(code,)
    cursor.execute(sql,val)
    clrscr()
    print("PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\tcode \t name\t\t price\t quantity\t category")
    print("\t\t","-"*47)
    for i in cursor:
        print("\t",i[0],"\t",i[1],"\t\t",i[2],"\t",i[3],"\t",i[4])
        print("\t\t","-"*47)
        
def list_prcat(cat):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    print(cat)
    sql="SELECT * from product WHERE pcat=%s"
    val=(cat,)
    cursor.execute(sql,val)
    clrscr()
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\tcode \t name\t\t price\t quantity\t category")
    print("\t\t","-"*47)
    for i in cursor:
        print("\t",i[0],"\t",i[1],"\t\t",i[2],"\t",i[3],"\t",i[4])
        print("\t\t","-"*47)

def clrscr():
    print("\n"*5) 

def add_mbr():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    cursor.execute("SELECT count(*) from mbr;")
    for i in cursor:
        a=i[0]
    sql="INSERT INTO mbr values(%s,%s,%s,%s)"
    code= 100+int(a)
    name=input("enter your name")
    sprice=0
    cat=input("enter the category: GOLD/SILVER").upper()
    if cat=="GOLD":
        print("collect Rs. 1000")
    elif cat=="SILVER":
        print("Collect Rs 500")
    else:
        print("enter a valid category")
    val=(code,name,sprice,cat)
    cursor.execute(sql,val)
    mydb.commit()
 
def list_mbr():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="rimiusessoft@8800",database="stock")
    cursor=mydb.cursor()
    while True:
        print("1.List all members")
        print("2. List members code wise")
        print("3.List members category wise")
        print("4.BACK")
        ch=int(input("Enter your choice:"))
        if ch==1:
            cursor.execute("SELECT * FROM mbr;")
            print(20*"****")
            print("memberid\t\tname\t\t times benefit availed\t\tCategory\t\t")
            print(20*"****")
            for x in cursor:
                print(x[0],"\t",x[1],"\t\t","\t\t",x[2],"\t\t",x[3])
                print()
        if ch==2:
            c=int(input("enter the code"))
            print(20*"****")
            print("memberid\t\tname\t\t times benefit availed\t\tCategory\t\t")
            sql="SELECT * FROM mbr where mbrid=%s;"
            val=(c,)
            cursor.execute(sql,val)
            print(20*"****")
            for x in cursor:
                print(x[0],"\t",x[1],"\t\t",x[2],"\t",x[3])
        if ch==3:
            ca=input("enter the category")
            print(20*"****")
            print("memberid\t\tname\t\t times benefit availed\t\tCategory\t\t")
            print(20*"****")
            cursor.execute("SELECT * FROM mbr where mcat=%s;",(ca,))
            for x in cursor:
                print(x[0],"\t",x[1],"\t\t",x[2],"\t\t",x[3])
                
        if ch==4:
            break

    
clrscr()
print(20*"****")
print("\t\t\t GROCERY MANAGEMENT SYSYTEM")
print("\t\t\t Dev by: our group SIV")
login()    
while True:
    print(40*"**","\n\n")
    print("\t\t\t1.DATABASE MANAGEMENT")
    print("\t\t\t2.USER MANAGEMENT")
    print("\t\t\t3.PRODUCT MANAGEMENT")
    print("\t\t\t4.SALES MANAGEMENT")
    print("\t\t\t5.MEMBERSHIP MANAGEMENT")
    print("\t\t\t6.ANALYSIS MANAGEMENT")
    print("\t\t\t7.EXIT")
    print(20*"****")
    print(20*"****")
    n=int(input("ENTER YOUR CHOICE:-"))
    print(20*"****")
    if n==3:
        product_mgmt()  
    if n==4:
        sales_mgmt()
    if n==2:
        user_mgmt()
    if n==1:
        db_mgmt()
    if n==5:
        mbr_ship()
    if n==6:
        ana_lys()
    if n==7:
        print("You have sucessfully exited the program")
        break
