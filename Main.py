from passengerinfo import*
from TicketShow import*
from admin import*
from payment import*

global ch # declare global variable
global y 
y = "no"

print("-----------------------------------------------------")
print("              Welcome to BusKita                     ")
print("-----------------------------------------------------")
print()

def menu():
    global ch
    ch = False
    print("1. Buat Akun Baru")
    print("2. Login       ")
    print("3. Exit ")
    print()
    while ch == False:
        try:
            ch = int(input("Pilih sesuai dengan nomornya: "))
        except:
            print("Tolong hanya masukkan angka.")

def start(): #called function
    global ch
    adminObj = Admin()
    if ch == 1:
        #admin class object creation
        adminObj.adminRegistration()
        menu()
        start()
        
    elif ch == 2:
        if y == "no":
            adminObj.adminLogin()
        elif y == "yes":
            adminObj.second_Log()
        
        choice = False
        print()
        print("1. Pesan tiket")
        print("2. Lihat tiket")
        print()
        while choice == False:
            try:
                choice = int(input("Pilih opsi: "))
            except:
                print("Tolong hanya masukkan angka.")
        if choice == 1:
            pd_obj = PassengerDataCsv()
            pd_obj.getPassengerInfo()
            pd_obj.saveInfo()
            choose_payment_method()
              
        elif choice == 2:
            obj = TicketShow()
            obj.ticketShow()
    elif ch == 3:
        print("Terima kasih telah menggunakan BusKita!")
    else:
        print("Perintah tidak tersedia silahkan masukkan ulang!")
        menu()
        start()

def pesan_lagi():
    global ch
    global y
    
    y = False
    while y == False:
        print("Apakah anda masih ingin berada di Aplikasi BusKita? [yes/no] ") 
        y = input("").lower()
        if y == "yes":
            print("-----------------------------------------------------")
            ch = 2
            start()
            pesan_lagi()
        elif y == "no":
            print("-----------------------------------------------------")
            print("Terima kasih telah menggunakan BusKita!")
            print("-----------------------------------------------------")
        else:
            print("Pilih yes/no saja!")

def main():
    menu()
    start()
    if ch !=3:
        pesan_lagi()
    
if __name__ == "__main__":
    main()
#calling function
#=======================================================================
