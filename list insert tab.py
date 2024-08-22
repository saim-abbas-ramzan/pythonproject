import mysql.connector as Myconn

mydb = Myconn.connect(host="localhost", user="root", password="saim51214", database="wscube")
db_cursor = mydb.cursor()
db_insert = "insert into student(id,name,email,age,status) values(%s,%s,%s,%s,%s)"
db_list = [(34, "saim", "@smgmail.com", 50, 4), (9, "jawad", "@jwagmail.com", 60, 6)]
db_cursor.executemany(db_insert, db_list)
mydb.commit()
print(db_cursor.rowcount, "Record inserted")

# list show the many data and age enter greater than 18 and everytime id & email diffrent insert