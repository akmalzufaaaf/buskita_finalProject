import csv
global user 
global passwd 

class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminRegistration(self):
        print("----------------------------------------------------------------")
        print()
        with open("adminCredential.csv",'a',newline="") as f:
            w =  csv.writer(f)
            self.username = input("Masukkan username    :")
            self.password = input("Masukkan password    :")
            #saving a data into database
            w.writerow([self.username,self.password])
            f.close()
            print("Registration successfully")
        print()
        print("----------------------------------------------------------------")
            
    def adminLogin(self):
        username = []
        password = []
        
        with open("adminCredential.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            #print(data)
            
            for i in data:
                username.append(i[0])
                password.append(i[1])

        #print(actList)
        while(True):
            global user
            global passwd
            
            print("----------------------------------------------------------------")
            print()
            self.username = input("Masukkan  username  :")
            self.password = input("Masukkan  password  :")
            for i in range(len(username)):
                if self.username == username[i] and self.password == password[i]:
                    user = username[i]
                    passwd = password[i]
                    print()
                    print("Login Succesfully!")
                    break
            else:
                print("Masukkan username dan password yang tepat!")
                continue
            
            print()
            print("---------------------------------------------------------------")
            break
        
    def second_Log(self):
        global user 
        global passwd
        
        username = []
        password = []
        
        with open("adminCredential.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            #print(data)
            
            for i in data:
                username.append(i[0])
                password.append(i[1])

        #print(actList)
        for i in range(len(username)):
            if user == username[i] and passwd == password[i]:
                break
            else:
                continue
