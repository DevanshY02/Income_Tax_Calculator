import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
mycursor = con.cursor()

def DataBaseSetup():
  mycursor.execute("DROP DATABASE IF EXISTS AHD")
  mycursor.execute("CREATE DATABASE AHD")
  mycursor.execute("USE AHD")
  print("Database AHD is active")
  mycursor.execute("DROP TABLE IF EXISTS emp")
  mycursor.execute("CREATE TABLE emp (eid int primary key, ename VARCHAR(30),  dept varchar(20), salary int, age int, gender CHAR(5))")
  print("Employee table created successfully....")

def InsertRecord():
   con = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
   mycursor = con.cursor()
   mycursor.execute("USE AHD")
   sql = """INSERT INTO emp VALUES(%s,%s,%s,%s,%s,%s)"""
   id=input("Enter Employee ID :  ")
   name=input("Enter your Name :  ")
   dept=input("Enter Department  Name :  ")
   sal=input("Enter Salaray of per annumn : ")
   age= (input("Enter your age "))
   gender=input("Enter gender M/F ")
   record=(id,name,dept,sal,age,gender) #tuple
   mycursor.execute(sql,record)
   print("Record inserted")
   con.commit()
   con.close()

def SearchRecord():
  con = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
  mycursor = con.cursor()
  mycursor.execute("USE AHD")
  id=int(input("Enter Employee ID who's Record to be Search : "))
  query1 = "SELECT * FROM emp where eid=%s "%(id)
  mycursor.execute(query1)
  result = mycursor.fetchall()
  count=mycursor.rowcount
  print("Total no. of Records found : ",count)
  print("ID \tNAME \t Dept \t Salary \t  Age \t Gender")
  for row in result:
    print(row)
    id = row[0]
    name = row[1]
    dept = row[2]
    salary = row[3]
    age=row[4]
    gender = row[5]
    print("%s  \t %s  \t%s \t%s \t%s  \t%s" % (id,name,dept,salary,age,gender))
  con.close()

def UpdateRecord():
  con = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
  mycursor = con.cursor()
  mycursor.execute("USE AHD")
  id=(input("Enter Employee ID who's Record to be update : "))
  query1 = "SELECT * FROM emp where eid=%s "%(id)
  mycursor.execute(query1)
  result = mycursor.fetchall()
  count=mycursor.rowcount # Return 0 if no record is found,otherwise return no. of Records found
  if count:
    query2="delete  FROM emp where eid=%s "%(id)
    mycursor.execute(query2)# Deleting old record
    print("Record is Found")
    print("ID \tNAME \t Dept \t Salary \t  Age \t Gender")
    print(result)
    sql = """INSERT INTO emp VALUES(%s,%s,%s,%s,%s,%s)"""
    id=input("Enter Employee ID :  ")
    name=input("Enter your Name :  ")
    dept=input("Enter Department  Name :  ")
    sal=input("Enter Salaray of per annumn : ")
    age= (input("Enter your age "))
    gender=input("Enter gender M/F ")
    record=(id,name,dept,sal,age,gender) #tuple
    mycursor.execute(sql,record)
    print("Record Updated Successfully...\n")
  else:
    print("Record is not found...\n")
  con.commit()
  con.close()

def DeleteRecord():
  con = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
  mycursor = con.cursor()
  mycursor.execute("USE AHD")
  id=(input("Enter Employee ID who's Record to be Delete : "))
  query1 = "SELECT * FROM emp where eid=%s "%(id)
  mycursor.execute(query1)
  result = mycursor.fetchall()
  count=mycursor.rowcount # Return 0 if no record is found,otherwise return no. of Records found
  if count: 
    print("Record is Found")
    print("ID \tNAME \t Dept \t Salary \t  Age \t Gender")
    print(result)
    query2="delete  FROM emp where eid=%s "%(id)
    mycursor.execute(query2)# Deleting old record
    print("Record Deleted  Successfully...\n")
  else:
    print("Record is not found...\n")
  con.commit()
  con.close()
  
def DisplayAll():
  con = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
  mycursor = con.cursor()
  mycursor.execute("USE AHD")
  sql = "SELECT * FROM emp"
  mycursor.execute(sql)
  result = mycursor.fetchall()
  print("ID \tNAME \t Dept \t Salary \t  Age \t Gender")
  for row in result:
    #print(row)
      id = row[0]
      name = row[1]
      dept = row[2]
      salary = row[3]
      age=row[4]
      gender = row[5]
      print("%s  \t %s  \t%s \t%s \t%s  \t%s" % (id,name,dept,salary,age,gender))
  con.close()

def TaxCal():
  con = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
  mycursor = con.cursor()
  mycursor.execute("USE AHD")
  id=int(input("Enter Employee ID who's Income Tax  to be Calculated : "))
  query1 = "SELECT * FROM emp where eid=%s "%(id)
  mycursor.execute(query1)
  result = mycursor.fetchall()
  if result:
      print("\nID \tNAME \t Dept \t Salary \t  Age \t Gender")
      print("_________________________________________________________")   
      for row in result:
      #print(row)
        id = row[0]
        name = row[1]
        dept = row[2]
        income = row[3]
        age=row[4]
        gender = row[5]
        print("%s  \t %s  \t%s \t%s \t%s  \t%s" % (id,name,dept,income,age,gender))
        if income <= 250000:
          tax = 0
        elif income <= 500000:  
          tax = (income-250000)* 0.05  
        elif income <= 1250000:
          tax =  (income-500000)* 0.1 +75000
        elif income <= 1500000:
            tax = (income -1250000)  * 0.2  +125000
        else:
            tax = (income-1500000)*0.3    + 187500
            print("_________________________________________________________")   
            print("\t\t",name," You owe Rs.", tax, " in tax!" )
  else:
    print("No Record is found...")

def ViewTaxSlab():
  slab='''   Income Tax Slab	            Individuals below the age of 60 years
  Up to Rs2,50,000	                Nil
  Rs2,50,001 to Rs5,00,000	        5% of total income exceeding
  Rs5,00,001 to Rs10,00,000	        12,500 + 10% of total income exceeding 5,00,000 
  Rs10,00,000 to Rs12,50,000         75000 + 20% of total income exceeding 10,00,000
  Rs12,50,001 to Rs15,00,000	      125000 + 25% of total income exceeding 12,50,000
  Above   Rs15,00,000	              187500 + 30% of total income exceeding  15,00,000'''
  print(slab)

def MainMenu():
  while True:
    print("_________________________________________________________")
    print('\n WELCOME   TO   INCOME TAX & EMPLOYEE MGT SYSTEM')
    print("_________________________________________________________")
    print("1. Setup Database & Table ")
    print("2. Add Record   ")
    print("3. Search / View Record  ")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Display All Record ")
    print("7. Calculate Tax ")
    print("8. View Tax Slab")
    print("0. Exit")
    choice=int(input("Enter your Choice : "))
    if choice==1:
      DataBaseSetup()
    elif choice==2:
      InsertRecord()
    elif choice==3:
      SearchRecord()
    elif choice==4:
      UpdateRecord()
    elif choice==5:
      DeleteRecord()
    elif choice==6:
      DisplayAll()
    elif choice==7:
      TaxCal()
    elif choice==8:
      ViewTaxSlab()
    elif choice==0:
      exit(0)
    else:print("Wrong input Try again")
MainMenu()