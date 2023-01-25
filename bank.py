import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='root',database='altaf')

def openAcc():
    n=input("Enter Name : ")
    ac=input("Enter Account No: ")
    db=input("Enter D.O.B : ")
    p=input("Enter Phone : ")
    ad=input("Enter Address : ")
    ob=int(input("Enter Opening Balance : "))
    data1=(n,ac,db,p,ad,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("\n\nData Entered Successfully")
    main()  
    
def depoAmo():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account No : ")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0] + am
    sql="update amount set balance =%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,d)

    con.commit()
    print("\n\n amount deposit successfull")
    main()

def withAm():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account No: ")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance=%s where acno =%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("withrall successfull")
    main()

def balance():
    ac=input("Enter Account No : ")
    a="select balance from amount where acno =%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for Account : ",ac,"is",myresult[0])
    main()

def dispacc():
    ac=input("Enter Account No : ")
    a="select * from account where acno = %s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=" ")
    main()

def closeac():
    ac=input("Enter Account No : ")
    sql1="delete from account where acno =%s"
    sql2="delete from account where acno =%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()

def main():
    print(""" \n\n Bank management system project \n\n
    1. OPEN NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE AN ACCOUNT
    """)
    choice=input("Enter Task No : ")
    while True:
       if(choice == '1'):
           openAcc()
       elif(choice=='2'):
           depoAmo()
       elif(choice=='3'):
           withAm()
       elif(choice=='4'):
           balance()
       elif(choice=='5'):
           dispacc()
       elif(choice=='6'):
           closeac()
       else:
           print("Wrong choice.....")
           main()

main()
           
    
