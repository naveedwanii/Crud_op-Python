import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', 
                                     port='3306',
                                     user='Naveed', 
                                     password='1234', 
                                     database='Student')
        query='create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print('created')


    def insert_student(self, studentid, studentname, phone):
        query= "insert into user(userId,userName,phone) values({},'{}','{}')".format(studentid,studentname,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('user saved to db')
  


    def fetch_all(self):
        query='select * from user'
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Student Id: ", row[0])
            print("Student Name:", row[1])
            print("Student Phone:", row[2])
            print()
            print()

    def delete_user(self, userId):
        query = "delete from user where userId ={}".format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print('Deleted')

    def update_user(self,userId,newName,newPhone):
        query = "update user set userName='{}',phone='{}' where userId={}".format(newName,newPhone,userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Student Updated')

