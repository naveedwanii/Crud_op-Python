 
"""
helper = DBHelper()
#helper.insert_student(5454,'Naveed','9149')
#helper.insert_student(6547,'Shahnoor','9858')
#helper.insert_student(7580,'Suhail','9909')
#helper.insert_student(4900,'Nazir','94199')
#helper.fetch_all()
#helper.delete_user(4900)
#helper.fetch_all()
helper.update_user(78,'Mehreen','9555')
helper.fetch_all()
"""
from dbhelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print('Welcome')
        print()
        print('Press 1 to insert new Student')
        print('Press 2 to display all Student')
        print('Press 3 to delete Student')
        print('Press 4 to update Studentt')
        print('Press 5 to exit program')
        print()
        try:
            choice = int(input())
            if(choice == 1):
                #insert Student
                uid = int(input('Enter Student Id: '))
                studentname = str(input('Enter Student Name: '))
                phone = int(input('Enter Student Phone No: '))
                db.insert_student(uid, studentname, phone)
                
            elif choice == 2:
                #display Student
                db.fetch_all()
                pass
            elif choice == 3:
                #delete Student
                userid = int(input('Enter Student Id to which you want to delete'))
                db.delete_user(userid)
            elif choice == 4:
                #update user
                uid = int(input('Enter id of Student which you want to update: '))
                username = str(input('New Student Name: '))
                userphone = int(input('Enter New Student Ph Number: '))
                db.update_user
                pass
            elif choice == 5:
                break
            else: 
                print('Invalid Input ! Try Again')
        except Exception as e:
            print(e)
            print('Invalid Details ! Try Again')


if __name__ == '__main__':
    main()