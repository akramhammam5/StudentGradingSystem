import statistics as s
from pip._vendor.distlib.compat import raw_input
import os



System = {}
file = open("Added.txt","at+")
file2 = open("Signup.txt","at+")



def avg():
    name = input("Student Name: ")
    sum=0
    with open("Added.txt", "r"):
        lines = file.readlines()

    with open("Added.txt", "w"):
        for line in lines:
            if name in line:
                print(list(System.keys())
                [list(System.values()).index(name)])
                
    
def Enter(name,grade):
    System[name] = grade
    file.writelines(str(System))
    print(file.read())
    print()
    #file.close()

def Remove(name):
    with open("Added.txt", "r"):
        lines = file.readlines()

    with open("Added.txt", "w"):
        for line in lines:
            if line.strip("\n") != name:
                file.write(line)

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
            break

def Main():
    os.system("clear")
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
    elif choice == '3':
        avg()
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
        os.system("clear")
        Login()
    elif choice == '2':
        SignUp()
    elif choice == '3':
        Exit()
Start()



