import pymysql
import pymysql.cursors

mydb = pymysql.connect(user='root',
                          password='1234',
                          host='localhost',
                          database='MyApp')
cursor = mydb.cursor()


users = {}
status = ""

#Præsenter menu
def displayMenu():
    status = input("Do you want to register? y/n?")
    if status == "y":
        addAccount()
    elif status == "n":
        print("Press q to quit")
    elif status == "show":

#Tilføj en bruger
        def addAccount():
            name = input("Create username: ")
            password = input ("Create password: ")
            if name in users:name
            print("This login name already exists")
    else:
        print("Login name successful")
        print("Press q to quit")
    
#Kald på menuen så den bliver fremvist
displayMenu()


# cursor.execute("SELECT* FROM profiles")
# results=cursor.fetchall()
# exist= cursor.fetchone()
# 
# query = ('INSERT INTO MyApp (Navn, Passw) VALUES (%s, %s);')
# cursor.execute(data, name, password)
# 
# mydb.commit()
# mydb.close()
