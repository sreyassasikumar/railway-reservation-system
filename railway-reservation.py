import time
import mysql.connector as con
from pwinput import pwinput 

mydb=con.connect(host="localhost",user="yourusername",password="yourpassword")
mycur=mydb.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS railway")
mycur.execute("USE railway")
mycur.execute("CREATE TABLE IF NOT EXISTS trains(train_id INT PRIMARY KEY,train_name VARCHAR(255),no_AC1st_class INT,no_AC2nd_class INT,no_AC3rd_class INT,no_sleeper_class INT,starting_point VARCHAR(255),destination VARCHAR(255));")
mycur.execute("CREATE TABLE IF NOT EXISTS bookings(booking_id INT AUTO_INCREMENT PRIMARY KEY,train_id INT,train_name VARCHAR(255),passenger_name VARCHAR(255),passenger_age INT,starting_point VARCHAR(255),destination VARCHAR(255),res_type VARCHAR(255),FOREIGN KEY(train_id) REFERENCES trains(train_id));")
mycur.execute("CREATE TABLE IF NOT EXISTS admin (username VARCHAR(255) PRIMARY KEY,password VARCHAR(255));")

#FUNCTIONS
#Adding train details
def utd():
    try:    
        trnam=input("enter the train name:")
        trno=int(input("Enter the train number:"))
        ac1=int(input("Enter the number of AC 1st class available:"))
        ac2=int(input("Enter the number of AC 2nd class available:"))
        ac3=int(input("Enter the number of AC 3rd class available:"))
        sl=int(input("Enter the number of sleeper class available:"))
        st=input("Enter the starting point:")
        en=input("Enter destination:")
        sql="INSERT INTO trains VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycur.execute(sql,(trno,trnam,ac1,ac2,ac3,sl,st,en))
        mydb.commit()
        print("loading",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("data successfully added")
        input("press enter to go back to home menu...")
    except EOFError as i:
        print(f'An error occured{i}')

#Display train details
def vtd():
    try:
        mycur.execute("select * from trains;")
        rec=mycur.fetchall()
        for i in rec:
            print("****************************")
            print("Train ID:",i[0],"\nTrain Name:",i[1],"\nSeats available AC1:",i[2],"\nSeats available AC2:",i[3],"\nSeats available AC3:",i[4],"\nSeats available SLEEPER:",i[5],"\nStarting point:",i[6],"\nDestination:",i[7])
        print("****************************")
    except EOFError as i:
        print(f'An error occured{i}')

#Delete train details
def dt():
    try:
        trno=int(input("enter the train number:"))
        mycur.execute(f"delete from bookings where train_id={trno}")
        mycur.execute(f"delete from trains where train_id={trno}")
        print("loading",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        mydb.commit()
        print("Data successfully deleted...")
        input("press enter to go back to home menu...")
    except EOFError as i:
        print(f'An error occured{i}')

#Reserve tickets
def rt():
    try:
        trno=int(input("enter the train number:"))
        trn=input("enter the train name:")
        st=input("enter the starting point:")
        ds=input("enter the destination:")
        mycur.execute(f"select * from trains where train_id={trno}")
        x=mycur.fetchone()
        print(f"1.AC 1st class\tSeats available : {x[2]}\n2.AC 2nd class\tSeats available : {x[3]}\n3.AC 3rd class\tSeats available : {x[4]}\n4.Sleeper class\tSeats available : {x[5]}")
        c=int(input("Enter your choice:"))
        time.sleep(1)
        if c==1:
            res="AC1"
            rest="No_AC1st_class"
            rate=4500
        elif c==2:
            res="AC2"
            rest="No_AC2nd_class"
            rate=2800
        elif c==3:
            res="AC3"
            rest="No_AC3rd_class"
            rate=1500
        elif c==4:
            res="Sleeper"
            rest="No_Sleeper_class"
            rate=800
        else:
            print("Wrong input")
        nos=int(input("Enter the number of seats:"))
        y=f"Select {rest}-%s from trains where train_id=%s"
        mycur.execute(y,(nos,trno))
        f=mycur.fetchone()
        f=f[0]
        print("Checking seat availability.",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(0.5)
        if f>=0:
            print("Seats available..")
            print(f"The rate for {nos} seat(s) in {trn} would be:{nos*rate}")
            input("Press enter to continue")
            print("Booking tickets.",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            for i in range(nos):
                nm=input("Enter the name of the passenger:")
                ag=int(input("Enter the age:"))
                time.sleep(1)
                v="insert into bookings(train_id,train_name,passenger_name,passenger_age,starting_point,destination,res_type) values(%s,%s,%s,%s,%s,%s,%s)"
                values=(trno,trn,nm,ag,st,ds,res)
                mycur.execute(v,values)
                mydb.commit()
                g="select booking_id from bookings where passenger_name=%s"
                nmm=[nm]
                mycur.execute(g,nmm)
                d=mycur.fetchone()
                print(f"Your PNR number:{d[0]}")
            print("loading",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            a=f"update trains set {rest}={rest}-%s where train_id=%s"
            mycur.execute(a,(nos,trno))
            time.sleep(1)
            print(f"Ticket successfully booked for {trn}")
            input("Press enter to return to home menu...")
        else:
            print("Seats unavailable...")
            print("Booking for general compartment")
            print("rate=100")
            print("loading",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            for i in range(nos):
                nm=input("Enter the name of the passenger:")
                ag=int(input("Enter the age:"))
                time.sleep(1)
                v="insert into bookings(train_id,train_name,passenger_name,passenger_age,starting_point,destination,res_type) values(%s,%s,%s,%s,%s,%s,%s)"
                values=(trno,trn,nm,ag,st,ds,'General')
                mycur.execute(v,values)
                mydb.commit()
            print(f"Ticket booked for {trn}")
    except EOFError as i:
        print(f"An error occured{i}")

#To show passenger list
def rts():
    mycur.execute("Select * from bookings;")
    f=mycur.fetchall()
    if len(f)==0:
        print("No seats reserved")
    else:
        n=1
        for i in f:
            print("************************")
            print(f"Passenger number:{i[0]}")
            print("Train ID:",i[1],"\nTrain Name:",i[2],"\nPassenger name:",i[3],"\nPassenger Age:",i[4],"\nStarting Point:",i[5],"\nDestination:",i[6],"\nReservation Type:",i[7])
        print("************************")

#Add a default admin user (only if the table is empty)
mycur.execute("SELECT COUNT(*) FROM admin;")
if mycur.fetchone()[0] == 0:
    while True:
        print("Create an admin user")
        u=input("Create admin username : ")
        ps=pwinput(prompt="Create admin password : ",mask="*")
        cp=pwinput(prompt="Confirm admin password : ",mask="*")
        if ps==cp:
            print("Creating admin user",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            mycur.execute("INSERT INTO admin (username, password) VALUES (%s,%s);",(u,ps))
            mydb.commit()
            print("Admin user created successfully")
            break
        else:
            print("Password doesn't match!")

#Admin login function
def admin_login():
    for i in range(3):
        username = input("Enter username : ")
        password = pwinput(prompt="Enter password : ",mask="*")
        y=(username, password)
        mycur.execute("SELECT * FROM admin WHERE username = %s AND password = %s;", y)
        #x=mycur.fetchone()
        if mycur.fetchone():
            return True
        else:
            print(f"Incorrect credentials. You have {2-i} attempts left.")
    else:    
        print("Too many failed attempts. Exiting...")
        return False

#Cancel tickets
def ct():
    try:
        pnr=int(input('Enter your PNR number:'))
        mycur.execute(f'Select * from bookings where booking_id={pnr};')
        data=mycur.fetchall()
        trno=int(input('Enter the train number:'))
        s=f'select res_type from bookings where booking_id={pnr}'
        mycur.execute(s)
        r=mycur.fetchone()
        r=r[0]
        if r=='AC1':
            rest="No_AC1st_class"
        elif r=='AC2':
            rest="No_AC2nd_class"
        elif r=='AC3':
            rest='No_AC3rd_class'
        elif r=='Sleeper':
            rest='No_Sleeper_class'
        print('Your details:')
        for i in data:
            print(i)
        if data==[]:
            print('No data found')
        else:
            mycur.execute(f'delete from bookings where booking_id={pnr};')
            mydb.commit()
            print("loading",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".")
            time.sleep(0.5)
            print('\nrefunding in progress please wait.',end='')
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".",end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            b=f'update trains set {rest}={rest}+1 where train_id={trno}'
            mycur.execute(b)
            mydb.commit()
            time.sleep(1)
            print('Data successfully deleted!!')
            input('Press enter to return to home menu....')
    except EOFError as i:
        print(f'An error occured{i}')



#MAIN PROGRAM
while True:
    print("\t\t\tRailway Reservation")
    print("\t\t\t  ===============")
    print("\t\t1.Admin login\n\t\t2.View train details")
    print('\t\t3.Reserve tickets\n\t\t4.Cancel tickets')
    print('\t\t5.Quit')
    uch=int(input('\t\tEnter your choice:'))
    if uch==1:
        #Admin_login()
        if admin_login()==True:
            print("Login successful.")
            while True:
                print("\t\t\t\t      Admin Mode")
                print("\t\t\t\t      ----------")
                print("\t\t\t\t1.Update train details\n\t\t\t\t2.Delete train details\n\t\t\t\t3.Show passenger list\n\t\t\t\t4.Quit admin mode")
                ch=int(input("Enter your choice : "))
                if ch==1:
                    utd()
                elif ch==2:
                    dt()
                elif ch==3:
                    rts()
                elif ch==4:
                    c=input("Do you want to quit admin mode(Y/N) : ")
                    if c.upper()=="Y":
                        break
    elif uch==2:
        vtd()
    elif uch==3:
        rt()
    elif uch==4:
        ct()
    elif uch==5:
        mycur.close()
        mydb.close()
        break
    else:
        print('Enter a valid option!')
