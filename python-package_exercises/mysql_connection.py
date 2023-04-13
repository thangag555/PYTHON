import mysql.connector as m
no = int(input("enter student no:"))
name = input("enter student name:")
course = input("enter course name:")
fees = int(input("enter fees:"))
myconn = m.connect(host="localhost", user="root", password="mySQL@2002", port=3306, database="ganesh")
cur = myconn.cursor()
sql = "insert into x1(no,name,course,fees)values(%s,%s,%s,%s)"
val = (no, name, course, fees)
try:
    cur.execute(sql, val)
    myconn.commit()
    
except:
    myconn.rollback()

print(cur.rowcount, "1 record inserted!")
myconn.close()
