
#!/usr/bin/python3
print("content-type: text/html")
print()

import os 
import getpass

os.system("tput setaf 1")
print("\t\tHello this is TUI project which will makes ur life simple")

os.system("tput setaf 7")
print("\t\t---------------------------------------------------------")

passwd = getpass.getpass("Enter ur password : ")
apass = "shruti"
if passwd != apass:
    print("authentication failure")
    exit()
    
while True:
    print("""
    Press 1  : To check date and time
    Press 2  : To check calander
    Press 3  : To long list files and directory of current directory
    Press 4  : To check user
    Press 5  : To check free space
    Press 6  : To create file
    Press 7  : To remove file
    Press 8  : To create directory
    press 9  : To remove directory
    Press 10 : To copy files or directory
    Press 11 : To move files or directory
    Press 12 : To create user
    Press 13 : To delete user
    Press 14 : To download anything form google
    Press 15 : To exit
    """)   

    print("enter ur choice : ",end="")
    ch=input()
    print(ch)
    if int(ch) == 1:
        os.system("date")
    elif int(ch) == 2:
        os.system("cal")
    elif int(ch) == 3:
        os.system("ls -l")
    elif int(ch) == 4:
        os.system("whoami")
    elif int(ch) == 5:
        os.system("free -m")
    elif int(ch) == 6:
        print("Enter path of file to be create")
        filename=input()
        os.system("touch {}".format(filename))
        print("File created successfully..")
    elif int(ch) == 7:
        print("Enter path of file to be remove")
        filename=input()
        os.system("rm {}".format(filename))
        print("File removed successfully..")
    elif int(ch) == 8:
        print("Enter path of directory to be create")
        dirname=input()
        os.system("mkdir {}".format(dirname))
        print("Directory created successfully")
    elif int(ch) == 9:
        print("Enter path of directory to be remove")
        dirname=input()
        os.system("rmdir {}".format(dirname))
        print("Directory removed successfully")
    elif int(ch) == 10:
        print("Enter source path")
        spath=input()
        print("Enter destination path")
        dpath=input()
        os.system("cp {} {}".format(spath,dpath))
        print("File or directory copied successfully..")
    elif int(ch) == 11:
        print("Enter source path")
        spath=input()
        print("Enter destination path")
        dpath=input()
        os.system("mv {} {}".format(spath,dpath))
        print("File or directory moved successfully..")
    elif int(ch) == 12:
        print("Enter username")
        username=input()
        os.system("useradd {}".format(username))
        print("Useradd successfully..")
    elif int(ch) == 13:
        print("Enter username")
        username=input()
        os.system("userdel {}".format(username))
        print("User removed successfully..")
    elif int(ch) == 14:
        print("Enter url")
        url=input()
        os.system("wget {}".format(url))
        print("Downloaded successfully..")
    elif int(ch) == 15:
        exit()
    else:
        print("Does not support")
