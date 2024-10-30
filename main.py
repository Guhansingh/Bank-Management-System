import mysql.connector

mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='4752',
                             database='bank_management')


def openacc():
    import random
    ac=str(random.randrange(1000000000,9999999999))
    n=input("Enter the Name: ")
    db=input("Enter the date of birth: ")
    add=input("Enter the Address: ")
    cn=input("Enter the Contact Number: ")
    ob=int(input("Enter the Opening Balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    mycursor=mydb.cursor()
    mycursor.execute(sql1,data1)
    mycursor.execute(sql2,data2)
    mydb.commit()
    print('Details inserted Sucessfully')
    main()

def deposit():
    amount=int(input("Enter the Amount to deposit: "))
    ac=input("Enter the Account Number: ")
    a='select Balance from amount where AccNo=%s'
    data=(ac,)
    mycursor=mydb.cursor()
    mycursor.execute(a,data)
    result=mycursor.fetchone()
    t=result[0]+amount
    sql='update amount set Balance=%s where AccNo=%s'
    d=(t,ac)
    mycursor.execute(sql,d)
    mydb.commit()
    main()

def withdraw():
    amount=int(input("Enter the Amount to Withdraw: "))
    ac=input("Enter the Account Number: ")
    a='select Balance from amount where AccNo=%s'
    data=(ac,)
    mycursor=mydb.cursor()
    mycursor.execute(a,data)
    result=mycursor.fetchone()
    t=result[0]-amount
    sql='update amount set Balance=%s where AccNo=%s'
    d=(t,ac)
    mycursor.execute(sql,d)
    mydb.commit()
    main()

def balance():
    try:
        ac=input("Enter the Account No: ")
        a='select*from amount where AccNo=%s'
        data=(ac,)
        mycursor=mydb.cursor()
        mycursor.execute(a,data)
        result=mycursor.fetchone()
        print("Balance for Account Number:",ac," is: ",result[-1])
        main()
    except:
        print("The has account doesn't exist")
        main()

def display():
    try:
        ac = input("Enter the Account No: ")
        a = 'select*from account where AccNo=%s'
        data = (ac,)
        mycursor = mydb.cursor()
        mycursor.execute(a, data)
        result = mycursor.fetchone()
        for i in result:
            print(i)
        main()
    except:
        print("The has account doesn't exist")
        main()

def close_acc():
    ac = input("Enter the Account No: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    mycursor=mydb.cursor()
    mycursor.execute(sql1,data)
    mycursor.execute(sql2,data)
    mydb.commit()
    main()


def main():
    print( '''
        
        1.OPEN NEW ACCOUNT
        2.DEPOSIT AMOUNT
        3.WITHDRAW AMOUNT
        4.BALANCE ENQUIRY
        5.DISPLAY CUSTOMER DETAILS
        6.CLOSE AN ACCOUNT''')

    choice=int(input('Enter the choice to perform: '))
    if choice==1:
        openacc()
    elif choice==2:
        deposit()
    elif choice==3:
        withdraw()
    elif choice==4:
        balance()
    elif choice==5:
        display()
    elif choice==6:
        close_acc()
    else:
        print("Invalid Choice!")
        main()
main()