import csv

class PaymentMethod:
    def __init__(self, method, details):
        self.method = method
        self.details = details

    def show_method(self):
        print("Payment Method: ", self.method)
        print("Payment Details: ", self.details)

def choose_payment_method():
    with open("passengerData.csv",'r+',newline="") as f:
        r =  csv.reader(f)
        data = list(r)
    total = int(data[-1][-1])
    id = int(data[-1][0])
     
    print()
    print("-----------------------------------------------------")
    print(f"Total yang harus dibayarkan : {total}")
    print("Pilih metode pembayaran:")
    print("1. Cash")
    print("2. Bank Transfer")
    print("3. E-Wallet")

    payment1 = PaymentMethod("Cash", "Bayarkan pada kasir")
    payment2 = PaymentMethod("Bank Transfer", "6798 1231 1234 1234 (Budi Santosi)")
    payment3 = PaymentMethod("E-Wallet", "1234 5678 9012 3456")

    try:
        choice = int(input("Masukkan pilihan: "))
        print("-----------------------------------------------------")
        print()

        if choice == 1:
            payment1.show_method()
        elif choice == 2:
            payment2.show_method()
        elif choice == 3:
            payment3.show_method()
        else:
            print("Pilihan tidak tersedia. Pilih 1, 2, atau 3.")
            print("-----------------------------------------------------")

    except ValueError:
        print("Masukkan nilai integer saja.")
        print("-----------------------------------------------------")
        print()
        choose_payment_method()
    
    print()
    print("Lihat detail tiket kamu pada menu Lihat Tiket!")
    print(f"ID Tiket : {id}")
    print("Selamat data kamu berhasil disimpan!")
