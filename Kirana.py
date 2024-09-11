
import json

import pandas as pd
import os
class EmailFormat(Exception):
    def __init__(self):
        print("please use valid email")
class PasswordFormat(Exception):
    def __init__(self):
        print("please enter a password with at least 8 character with once Uppercase and 2 digit")
class Kirana:
    def __init__(self):
        self.menu()

    def menu(self):
        print('*'*100,"Welcome to my Kirana Store",'*'*100,sep='\n')
        print()
        print('-'*30,"Please Choose user type",'-'*30,sep='\n')
        choice=input("""Are you a customer or a manager?\n1.Customer\n2.Owner\n3.Exit\n""")
 
        if choice=="1":
            Users()
        elif choice=="2":
            Owners()
        elif choice=="3":
            exit()
        else:
            print("Invalid input")
            self.menu()
    def menutype(self,choice):
        print('-'*30,"Please choose one of them",'-'*30,sep='\n')
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
            try:
                email=input("Enter email\n")
                if '@' not in email:
                    raise EmailFormat()
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
                        Flag=False
                        for k,v in data.items():
                            if k==email:
                                if password == v[1]:
                                    Flag=True
                                    print("Login successful")

                                else:
                                    print("Incorrect password")
                                    self.login(choice)
                        if Flag==False:    
                            print("You have not registered yet, please register")
                            self.menutype(choice)
            except EmailFormat as e:
                self.login(choice)

     
            
         
    def register(self,choice):
            try:
                name=input("Enter name\n")
                email=input("Enter email\n")
                if '@' not in email:
                    raise EmailFormat()
                password=input("Enter password\n")
                if  self.validpassword(password)==False:
                        raise PasswordFormat()
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
                            d={email:[name,password]}
                            data.update(d)
                            with open(file_path,"w") as f:
                                json.dump(data,f,indent=4)
                            print("Registration successful")
                        self.menutype(choice)

            except EmailFormat as e:
                self.register(choice)

            except PasswordFormat as e:
                self.register(choice)
    def logout(self):
        print("Come soon , Bye Bye")
        exit()

    def validpassword(self,password):
        if len(password)<8:
            return False
        else:
            digit=0
            upper=0
            for i in password:
                if i.isdigit():
                    digit+=1
                if i.isupper():
                    upper+=1
            if digit==2 and  upper ==1:
                return True
            return  False


class Users(Kirana):
    def __init__(self):
        self.menutype("1")
        self.buy()
    
    def buy(self):

        with open('product.json','r') as f:
            if os.path.getsize('product.json') == 0:
                print("No product available")
                self.logout()
            else:
                data=json.load(f)
                for k,v in data.items():
                    print(f"product id :{k} | product name :{v[0]} | price :{v[1]} | quantity :{v[2]}")
                if os.path.getsize('bill.json')!= 0:
                        with open('bill.json', 'w') as json_file:
                            json.dump([], json_file, indent=4)
                while True:
                    
                    
                    product_id=input("Enter product id\n")
                    if product_id in data.keys():
                        quantity=int(input("Enter quantity\n"))
                        if quantity<=int(data[product_id][2]):
                            finalbill={"Product ID":product_id,"Product Name":data[product_id][0],"Product Price":int(data[product_id][1]),"Quantity":int(quantity)}                    # bill.append([product_id,data[product_id][0],data[product_id][1],quantity])\\

                            if os.path.getsize('bill.json')== 0:
                                with open('bill.json', 'w') as file:
                                    json.dump([finalbill], file, indent=4)
                
                            else:
                                with open('bill.json','r') as f:
                                    d=json.load(f)
                                d.append(finalbill)
                                with open('bill.json','w') as f:
                                    json.dump(d,f,indent=4)
                        else:
                            print("Insufficient quantity")
                    else:
                        print("Invalid product id")
                    choice=input("Do you want to buy another product?\n")
                    if choice=="yes":
                        continue
                    else:
                        break
        self.bill()

    def bill(self):
        total=0
        with open('bill.json','r') as f:
            bill=json.load(f)
            for i in bill:
                total+=i["Product Price"]*i["Quantity"]
            print('-'*30,"Your bill is",'-'*30,sep='\n')
            print(total)
  
        with open('bill.json','w') as f:
            json.dump(bill,f,indent=4)

        with open('bill.json','r') as f:
            bill=json.load(f)
        df=pd.DataFrame(bill)
        df.to_csv('bill.csv',index=False)
        print('-'*30,"collect your bill",'-'*30,sep='\n')
        print("Thank you for shopping with us")
        self.logout()



class Owners(Kirana):
     def __init__(self):
        self.menutype("2")
        self.crud()
    
     def crud(self):
        choice=input("what you want to do ?\n1. Add product\n2. View product\n3. Update product\n4. Delete product\n5.Back to main menu\n6.Logout\n")
        if choice=="1":
            self.add()
        elif choice=="2":
            self.view()
        elif choice=="3":
            self.update()
        elif choice=="4":
            self.delete()
        elif choice=="5":
            self.menu()
        elif choice=="6":
            self.logout()
        else:
            print("Invalid input")
            self.crud()
        
     def add(self):
        product_id=input("Enter product id\n")
        product_name=input("Enter product name\n")
        product_price=int(input("Enter product price\n"))
        product_quantity=int(input("Enter product quantity\n"))
        with open("product.json","r") as f:
            if os.path.getsize("product.json") == 0:
                data={product_id:[product_name,int(product_price),int(product_quantity)]}
                with open("product.json","w") as f:
                    json.dump(data,f,indent=4)
            else:
                with open("product.json","r") as f:
                    data=json.load(f)
                    data[product_id]=[product_name,int(product_price),int(product_quantity)]
                    with open("product.json","w") as f:
                        json.dump(data,f,indent=4)
        print("Product added successfully")
        self.crud()
     def view(self):
         with open('product.json','r') as f:
            if os.path.getsize('product.json') == 0:
                print("No product available")
                self.crud()
            else:
                data=json.load(f)
                for k,v in data.items():
                    print(f"product id :{k} | product name :{v[0]} | price :{v[1]} | quantity :{v[2]}")
                self.crud()

     def update(self):
         with open('product.json','r') as f:
            if os.path.getsize('product.json') == 0:
                print("No product available")
            else:
                id,name,price,quantity=input("enter product id , product name ,price and quantity to update").split()
                data=json.load(f)
                data[id]=[name,price,quantity]
                with open('product.json','w') as f:
                    json.dump(data,f,indent=4)
                print("Product updated successfully")
                self.crud()

     def delete(self):
         id=input("Enter product id to delete\n")
         with open('product.json','r') as f:
            if os.path.getsize('product.json') == 0:
                print("No product available")
            else:
                data=json.load(f)
                data.pop(id)
                with open('product.json','w') as f:
                    json.dump(data,f,indent=4)
                print("Product deleted successfully")
                self.crud()         
         
k = Kirana()

