import mysql.connector as Myconn

mydb=Myconn.connect(host="localhost",user="root",password="saim51214",database="wscube")
db_cursor=mydb.cursor()
db_updatedata="update wscube.student set age=%s where id=%s"
db_value=(25,5)
db_cursor.execute(db_updatedata,db_value)
mydb.commit()  #permanent changes save ho jye data, database mein
print("data updates!!")