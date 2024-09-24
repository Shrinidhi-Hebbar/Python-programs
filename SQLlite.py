#SQLlite
import sqlite3 as sql
con=sql.connect("example.db")
print("Database connected")
cur=con.cursor()
st="""
create table if not exist student
(
rno varchar(10),
name varchar(10),
primary key(rno)
)
"""
cur.execute(st)
con.commit()
print("Table created")
cur.execute("deleted student data")
con.commit()

print("Enter 5 student rollno and name")
for i in range(1,6):
    rno=input(f"Enter the {i} rollno of student")
    name=input(f"Enter {i} student name")
    cur.execute("insert into student(rno,name)value(? ?)",(rno,name))
    con.commit()
    print(f"{i} row inserted")

def display():
    global cur
    cur.execute("select * from student")
    result=cur.fethall()
    print("Student data are as fallows")
    print(f"Rollno|\t Student Name\t|")
    for row in result:
        rno=row[0]
        name=row[1]
        print(f"{rno}|\t{name}\t|")
print("After inserting row table data")
display()

print("Table data updation")
rno=input("Enter rollno of student you want to update")
name=input("Enter name of student you want to update")
cur.execute("update student set name=? where rno=?",(name,rno))
con.commit()
print("Table data updated successfully")
display()

print("table row deletetion")
rno=input("Enter rollno of student you want to delete")
cur.execute("delete from student where rno=?",(rno))
con.commit()
print("Table data deleted successfully")
print("After deleting row table data ")
display()

con.close()
print("Connection closed")

