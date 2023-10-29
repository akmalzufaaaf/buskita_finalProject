import csv

class RegistrasiUser():
    #constructor
    def __init__(self):
        self.namaPenumpang = None
        self.jumlahPenumpang = None
        self.lokasiKeberangkatan = None
        self.lokasiTujuan = None
        self.ddmmyyyy = None
        self.nomorKursi = None
        self.tipeBus = None
        self.ongkosBus = None
        self.autoInc = 1 # ??
        self.countcol= 0 #??
        
    def getPassengerInfo(self):
        self.namaPenumpang = input("Masukkan Nama Penumpang     :")
        self.jumlahPenumpang = int(input("Masukkan Jumlah Penumpang :"))
        print("1: Giwangan")
        print("2: Jombor")
        print("3: Gamping")
        print("4: Adisutjipto")

        # Enter departure Location Name START
        self.dl = int(input("Masukkan Lokasi Keberangkatan: "))
        if self.dl == 1:
            self.lokasiKeberangkatan = "Giwangan"
        elif self.dl == 2:
            self.lokasiKeberangkatan = "Jombor"
        elif self.dl == 3:
            self.lokasiKeberangkatan = "Gamping"
        elif self.dl == 4:
            self.lokasiKeberangkatan = "Adisujibto"
        else:
            print("Aplikasi tidak mendukung untuk keberangkatan melalui Terminal {}".format(self.lokasiKeberangkatan))
        # departure Location Name END
        
        print("1: Giwangan")
        print("2: Jombor")
        print("3: Gamping")
        print("4: Adisutjipto")
        # Enter destination Location Name START
        self.dpl = int(input("Masukkan destinasi:"))
        if self.dpl == 1:
            self.lokasiTujuan = "Giwangan"
        elif self.dpl == 2:
            self.lokasiTujuan = "Jombor"
        elif self.dpl == 3:
            self.lokasiTujuan = "Gamping"
        elif self.dpl == 4:
            self.lokasiTujuan = "Adisutjipto"
        # Enter destination Location Name END

        self.ddmmyyyy = input("Masukkan tanggal keberangkatan, misal 07-05-1992   :")  #Date of Journey

        #Booking Seat Start 
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        nomorKursiList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
        while True:
            self.nomorKursi = int(input("Pilih Nomor Kursi & Maksimal Anda Dapat Memesan Dua Tiket  :"))
            if self.nomorKursi <=30:
                if  self.nomorKursi in nomorKursiList:
                    self.bookingList.append(self.nomorKursi)
                    del nomorKursiList[self.nomorKursi+1]
                    count = len(nomorKursiList)
                else:
                    print("Kursi sudah dipesan.")
                print("Apakah kamu mau memesan tiket lagi (Yes/No)") 
                y = input("") 
                if y == "Yes":
                    pass # belum ada kode
                else:
                    break

            else:
                print("Nomor kursi tidak tersedia.")    
        # Booking Seat END
        
        print(" 1. Bus Eksekutif")
        print(" 2. Bus Ekonomi")
        self.tipeBus = int(input("Pilih Tipe Bus : "))
        
        if self.tipeBus == 1:
            self.selecttipeBus = "AC BUS"
            self.busFare = self.noOfPassenger*500
        elif self.tipeBus == 2:
            self.selecttipeBus = "NON AC BUS"
            self.busFare = self.noOfPassenger*300
           
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
                w.writerow([self.autoInc,self.passengerName,self.noOfPassenger,self.lokasiKeberangkatan,self.lokasiTujuan,self.ddmmyyyy,self.bookingList,self.selecttipeBus,self.busFare])
                print("Data Save successfully")
                print()
        

'''pd_obj = PassengerDataCsv()
pd_obj.getPassengerInfo()
pd_obj.saveInfo()'''