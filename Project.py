import statistics as s
from pip._vendor.distlib.compat import raw_input

System = {}
file = open("Added.txt","at+")
file2 = open("Signup.txt","at+")

def Enter(name,grade):
    System[name] = grade
    file.writelines(str(System))
    print(file.read())
    print()
    file.close()

def Remove(name):
    System.pop(name)

def Exit():
    print("\nThank You for Using our system :)\n")
    quit()

def Show():
    print(file.read())


def SignUp():
    print("***********************************Sign Up*****************************************\n")

    uname = input("Enter your username: ")
    password = input ("Enter your password: ")
    file2.writelines("username: ")
    file2.writelines(uname)
    file2.write("\n")
    file2.writelines("password: ")
    file2.writelines(password)
    file2.write("\n")
    file.close()
    print("Thx for choosing our system :)")
    Login()


def Login():
    print("***********************************Login*****************************************\n")

    uname = raw_input("Username: ")
    password = raw_input ("Password: ")
    f = open("Signup.txt", "r+")
    lines = f.readlines()
    for line in lines:
        if uname in line:
            Main()
        else:
            print("you are not a registered")
            f.close()
            break

def Main():
    print("                      Welcome to Grade Central\n")

    print("[1] - Enter Grades")
    print("[2] - Remove Student")
    print("[3] - Student Average Grades")
    print("[4] - Show all students with their grades")
    print("[5] - Exit")

    choice = input("What would you like to do today? (Enter a number): ")

    if choice == '1':
            name = input("Student Name: ")
            grade = input("Grade: ")
            print("Adding Grade...")
            Enter(name,grade)
    elif choice == '2':
            name = input("Student Name: ")
            Remove(name)
    elif choice == '4':
            Show()
    elif choice == '5':
            Exit()
    else:
            print("Invalid Input")


def Start():
    print("                      Welcome to Grade Central\n")

    print("[1] - Login")
    print("[2] - Sign Up")
    print("[3] - Exit")

    choice = input("What would you like to do? (Enter a number): ")

    if choice == '1':
        Login()
    elif choice == '2':
        SignUp()
    elif choice == '3':
        Exit()
Start()



