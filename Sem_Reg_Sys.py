students={100:{"name":"Neeyat Basnet","pass":123,"enrolled":["CD","SE"]},101:{"name":"Anmol Boruah","pass":456,"enrolled":[]}}
#print(students[476]["Dept"])
courses={5:{"FLAT":3,"OS":4,"CNS":12,"CN":2,"SDC":9},6:{"CD":11,"SE":5,"CC":4,"RL":7,"NEDM":2}}
#print(courses[6][1])
# students[1]["enrolled"].append("xyz")
# print(students[1])

def registration():
    #global usr_id
    id=int(input("Enter new user id"))
    if id in students:
        print("Already Registered")
        return None
    n=input("Enter your name:")
    p=int(input("Enter your new password:"))
    students[id]={"name":n,"pass":p,"enrolled":[]}
    print("Registered Successfully")

def login():
    global usr_id
    usr_id=int(input("Enter user id:"))
    p=int(input("Enter your password:"))
    if usr_id in students:
        if students[usr_id]["pass"]==p:
            print("Logged in successfully")
            return 1
        else:
            print("Wrong password")
            return None
    else:
        print("Invalid id")
        return None

def avaiCourses():
    sem=int(input("Enter your sem:"))
    print("__Available Courses and seats respectively __")
    if sem in courses:
        print(courses[sem])

#courses[6]["CD"]-=1

def enrollment():
    #id=int(input("Enter reg id:"))
    sem=int(input("Enter your sem:"))
    print("___Select from the following set of available courses__")
    print(courses[sem])
    ch=input("Enter your opted course:").upper()
    for course in students[usr_id]["enrolled"]:
        if course==ch:
            print("Already enrolled in this course:")
            return None
    if courses[sem][ch]>0:
        courses[sem][ch]-=1
        students[usr_id]["enrolled"].append(ch)
        print("Successfully enrolled")
        #print(students)
        return None
    else:
        print("Opted course is already full")

def drop():
    #id=int(input("Enter reg id:"))
    #sem=int(input("Enter your sem:"))
    course=input("Enter the course you want to drop:").upper()
    print(students[100]["enrolled"])
    if course not in students[usr_id]["enrolled"]:
        print(f"You haven't enrolled in {course} to drop it")
        return None
    students[usr_id]["enrolled"].remove(course)
    print("Course dropped out successfully")


def regGeneration():
    flag=True
    #id=int(input("Enter reg id:"))
    if usr_id not in students:
        print("Not Registered")
        return None
    print("__Registration Confirmation__")
    print("Reg id:",usr_id)
    print("Name:",students[usr_id]["name"])
    print("Enrolled in:",end='')
    for course in students[usr_id]["enrolled"]:
        flag=False
        print(course,end=' ')
    if flag:
        print("Null")

def admin():
    #x=input("Enter password:")
    password="admin123"
    if(input("Enter password:")!=password):
        print("Invalid Password")
        return None
    else:
        while(True):
            ch=int(input("\nEnter your choice\n1.Add course\n2.Remove course\n3.Delete student records\n4.View student records and courses\n5.Logout\nYour Choice->"))
            if ch==1:
                sem=int(input("Enter sem:"))
                cour=input("Enter course:").upper()
                seats=int(input("Enter seats:"))
                courses[sem][cour]=seats
                print("Added Successfully")
            elif ch==2:
                sem=int(input("Enter sem:"))
                cour=input("Enter course:").upper()
                del courses[sem][cour]
                print("Deleted Successfully")
            elif ch==3:
                sid=int(input("Enter id:"))
                del students[sid]
                print("Removed")
            elif ch==4:
                print("__STUDENT RECORDS__\n",students)
                print("__COURSES__\n",courses)

            else:
                print("Logged out from Admin Management")
                return None


while(True):
    ch=int(input("\nEnter\n1.Admin\n2.User Registration\n3.User Login\n4.End\nYour choice->"))
    if ch==1:
        admin()
    elif ch==2:
        registration()
        print("To avail services please login in to your account")
    elif ch==3:
        if login():
            while(True):
                choice=int(input("\n\nEnter\n1.view available courses\n2.enroll in a course\n3.drop a course\n4.generate registration confirmation\n5.Logout\nYour Choice->"))
                if choice==1:
                    avaiCourses()
                elif choice==2:
                    enrollment()
                elif choice==3:
                    drop()
                elif choice==4:
                    regGeneration()
                else:
                    print("Logged out successfully")
                    break    
    
    elif ch==4:
        print("Closing the system")
        break
