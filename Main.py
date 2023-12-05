from passengerinfo import*
from TicketShow import*
from admin import*
from payment import*

global ch # declare global variable
y = "no"

print("-----------------------------------------------------")
print("              Welcome to BusKita                     ")
print("-----------------------------------------------------")
print()

def menu():
    global ch
    print("1. Buat Akun Baru")
    print("2. Login       ")
    print("3. Exit ")
    print()
    ch = int(input("Pilih sesuai dengan nomornya: "))

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
        
        print()
        print("1. Pesan tiket")
        print("2. Lihat tiket")
        print()
        ch = int(input("Pilih opsi: "))
        if ch == 1:
            pd_obj = PassengerDataCsv()
            pd_obj.getPassengerInfo()
            pd_obj.saveInfo()
            choose_payment_method()
              
        elif ch == 2:
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
    print("Apakah anda masih ingin berada di Aplikasi BusKita? [yes/no] ") 
    y = input("").lower()
    if y == "yes":
        ch = 2
        start()
        pesan_lagi()
    elif y == "no":
        print("Terima kasih telah menggunakan BusKita!")
    else:
        print("Pilih yes/no saja!")

if __name__ == "__main__":
    menu()
    start()
    pesan_lagi()
    
#calling function
#=======================================================================
