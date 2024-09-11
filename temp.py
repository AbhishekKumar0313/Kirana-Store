import json
import os
class Kirana:
    def __init__(self):
        self.menu()

    def menu(self):
        choice=input("""Are you a customer or a manager?\n1.Customer\n2.Owner\n3.Exit\n""")
        if choice=="1" or choice=="2":
            self.menutype(choice)
        elif choice=="3":
            exit()
        else:
            print("Invalid input")
            self.menu()
    def menutype(self,choice):
        c_choice=input("""1.Login \n2.Register\n3.Back to main menu\n""")
        if c_choice=="1":
            self.login(choice)
        elif c_choice=="2":
            self.register(choice)
        elif c_choice=="3":
            self.menu()
        else:
            print("Invalid Input")
            self.menutype()
   
    def login(self,choice):
            email=input("Enter email\n")
            password=input("Enter password\n")
            if choice=="1":
                file_path='users.json'
            else:
                file_path='owner.json'
            with open(file_path,"r") as f:
                if os.path.getsize(file_path) == 0:
                    print("You have not registered yet, please register as user")
                    self.menu()
                else:
                    data=json.load(f)
                    for k,v in data.items():
                        if k==email:
                            if password  in v:
                                print("Login successful")
                            else:
                                print("Incorrect password")
                                self.login(choice)
                        else:
                            print("You have not registered yet, please register")
                            self.register(choice)
         
    def register(self,choice):
            name=input("Enter name\n")
            email=input("Enter email\n")
            password=input("Enter password\n")
            if choice=="1":
                file_path='users.json'
            else:
                file_path='owner.json'
            if os.path.getsize(file_path)== 0:
                d={email:[name,password]}
                with open(file_path, 'w') as file:
                    json.dump(d, file, indent=4)
                    print("Registration successful")
                self.login(choice)
            else:
                with open(file_path,"r") as f:
                    data=json.load(f)
                    if email in data.keys():
                        print("User already exists, please login")
                        self.login(choice)
                    else:
                        d={"email":[name,password]}
                        data.update(d)
                        with open(file_path,"w") as f:
                            json.dump(data,f,indent=4)
                        print("Registration successful")
                        self.login(choice)


class Users:
    pass


class Owner:
    pass
k = Kirana()

# tommorrow plan of action 
# a db for owner to add and user to view
