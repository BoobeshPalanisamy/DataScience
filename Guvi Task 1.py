#Task1
#Entry e-mail and password and validating

#Please enter your e-mail ID and Password
import re
val={"email":[],"Password":[]}

matcher=re.compile('[a-zA-Z0-9#$%&!_\-/]+@[a-z]+\.[a-z]+')
def register():
    import string
    pattern = r'^[' + string.punctuation + ']+'
    email=input("email: ")
    if email[0].isdigit()==True:
        print('Please enter Valid email ID')
        register()
    elif re.search(pattern, email) is not None:
        print('Please enter Valid email ID')
        register()
    elif re.fullmatch(matcher, email):
        val["email"]=email
        val_pass()
    else:
        print('Please enter Valid email ID')
        register()

def val_pass():
    password=input("Password: ")
    l, u, d, s = 0, 0, 0, 0
    special_char="[$#@%&]'.:;{}^()!)"
    if len(password)>=5 and len(password)<=16:
        for i in password:
            if (i.islower()):
                l+=1
            if (i.isupper()):
                u+=1
            if (i.isdigit()):
                d+=1
            if (i in special_char):
                s+=1
    if (l>=1 and u>=1 and d>=1 and s>=1 and l+u+d+s==len(password)):
        val["Password"]=password
        store_data()
    else:
        print("Please enter Valid Password")
        val_pass()
        

def store_data():
    file = open('hello.txt','a')
    file.write(val["email"])
    file.write(" ")
    file.write(val["Password"])
    file.write("\n")
    file.close()
    login()
        
    
def login():
    file=open("hello.txt","r")
    line_list=file.readlines()
    file.close()
    
    info_dict={}
    
    for line in line_list:
        info=line.split()
        email=info[0]
        password=info[1]
        info_dict[email]=password
    
    email=input('please enter your email ID: ')
    password=input('please enter your password: ')
    
    if (email in info_dict):
        if info_dict[email]==password:
            print("Welcome!, You are logged in")
        else:
            print("Password is incorrect")
            forgotpass()
    else:
        print("Sorry, Given details not found,Please register and continue")
        register()
       
def forgotpass():

    fp=input("Enter 1 for reenter and 2 for know password and 3 for change password: ")
    if fp=='1':
        print("please enter login details")
        login()
        return True
    elif fp=='2':
        email=input('please enter your email ID: ')
        for i in open("hello.txt","r").readlines():
            file=i.split()
            if email==file[0]:
                print(file[1])
                login()
                return True
    elif fp=='3':
        print('please enter details')
        register()
        
register()