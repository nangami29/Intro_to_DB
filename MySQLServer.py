import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='nangamira1',
    
)
mycursor = mydb.cursor()

#create database
mycursor.execute("""
CREATE DATABASE IF NOT EXISTS alx_book_store

""")

print("Database 'alx_book_store' created successfully!")

# re-connect with the database created
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='nangami1',
    database = 'alx_book_store'

)
if 'connected':
    print(f"DB connected successfuly!")
else:
     print(f"except mysql.connector.Error")
          
          
#Execute sql statements using the execute() method on the cursor
# close connection to the database
mycursor.close()

mydb.close()
print(mydb.get_server_info())