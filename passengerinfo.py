import csv

class PassengerRegistration():
    #constructor
    def __init__(self):
        self.passengerName = None
        self.noOfPassenger = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.autoInc = 1
        self.countcol= 0
        
    def getPassengerInfo(self):
        self.passengerName     = input("Masukkan Nama :")
        self.noOfPassenger     = int(input("Masukkan Jumlah Penumpang :"))
        print("1: Giwangan")
        print("2: Jombor")
        print("3: Gamping")
        print("4: Adisutjipto")

        # Enter departure Location Name START
        self.dl = int(input("Masukkan Terminal Keberangkatan: "))
        if self.dl == 1:
            self.departureLocation = "Giwangan"
        elif self.dl == 2:
            self.departureLocation = "Jombor"
        elif self.dl == 3:
            self.departureLocation = "Gamping"
        elif self.dl == 4:
            self.departureLocation = "Adisutjipto"
        else:
            print("Masukkan pilihan yang tersedia..")
        # departure Location Name END
        
        print("1: Giwangan")
        print("2: Jombor")
        print("3: Gamping")
        print("4: Aditsutjipto")
        # Enter destination Location Name START
        self.dpl = int(input("Enter Destination Location  :"))
        if self.dpl == 1:
            self.destinationLocation = "Giwangan"
        elif self.dpl == 2:
            self.destinationLocation = "Jombor"
        elif self.dpl == 3:
            self.destinationLocation = "Gamping"
        elif self.dpl == 4:
            self.destinationLocation = "Aditsutjipto"
        # Enter destination Location Name END

        self.ddmmyyyy = input("Masukkan tanggal keberangkatan 07-05-1992 : ")  #Date of Journey

        #Booking Seat Start 
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
        while True:
            self.seatNo = int(input("Pilih nomor kursi: "))
            if self.seatNo <=30:
                if  self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo+1]
                    count = len(seatNoList)
                else:
                    print("Kursi sudah dipesan!")
                print("Apakah kamu ingin memesan tiket lagi [yes/no]? ") 
                y = input("").lower()
                if y == "yes":
                    pass
                else:
                    break
            else:
                print("Kursi yang dipilih tidak tersedia!")    
        # Booking Seat END
        
        print(" 1. Eksekutif : Rp 50.000,00")
        print(" 2. Ekonomi : Rp 15.000,00")
        self.busType = int(input("Pilih Tipe Bus : "))
        
        if self.busType == 1:
            self.selectBusType = "Eksekutif"
            self.busFare = self.noOfPassenger*50000
        elif self.busType == 2:
            self.selectBusType = "Ekonomi"
            self.busFare = self.noOfPassenger*15000
           
        # Booking Seat END
#=============================================
#saving Passenger Data into csv File
#=============================================
class PassengerDataCsv(PassengerRegistration):
    def saveInfo(self):
        try:
            with open("passengerData.csv",'r+',newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                #print(self.data)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("Number of Records Are Found In Database :",self.autoInc)    
            
        except:
            print("File has not available")
        finally:     
            with open("passengerData.csv",'a+',newline="") as f:
                w =  csv.writer(f)
                #w.writerow(["Auto Increment","passenger Name","Number of Passenger","Departure Location","Destination Location","ddmmyyyy","Seat No","Select Bus Type","Bus Fare"])
                w.writerow([self.autoInc,self.passengerName,self.noOfPassenger,self.departureLocation,self.destinationLocation,self.ddmmyyyy,self.bookingList,self.selectBusType,self.busFare])
                print("Data Save successfully")
                print()
        

'''pd_obj = PassengerDataCsv()
pd_obj.getPassengerInfo()
pd_obj.saveInfo()'''