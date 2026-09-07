def cek_saldo(saldo):
    print(f"Saldo anda: Rp.{saldo}")

def setor_tunai(saldo):
    jumlah = int(input("Masukkan jumlah setor: "))
    saldo += jumlah
    return saldo

def tarik_tunai(saldo):
    tarik = int(input("Masukkan jumlah tarik: "))
    if tarik > saldo:
        print("Saldo tidak mencukupi!")
    else:
        saldo -= tarik
        print(f"Saldo baru: Rp.{saldo}")
        
    return saldo
    
def ganti_pin(pin):
    pin_baru = input("Masukkan PIN baru: ")
    pin = pin_baru 
    print("PIN baru berhasil disimpan!!")
    return pin
    
def menu_atm(saldo, pin):
    ulang = True
    
    while ulang:
        print("+====================+")
        print("|         ATM        |")
        print("+====================+")
        print("| 1. Cek Saldo       |")
        print("| 2. Setor Tunai     |")
        print("| 3. Tarik Tunai     |")
        print("| 4. Ganti PIN       |")
        print("| 0. Keluar          |")
        print("+--------------------+")
        
        pilih = input("Pilih menu (0-4): ")
        
        match pilih:
            case "1":
                cek_saldo(saldo)
            case "2":
                saldo = setor_tunai(saldo)
            case "3":
                saldo = tarik_tunai(saldo)
            case "4":
                pin = ganti_pin(pin)
            case "0":
                print("Program selesai, Terima kasih!!!")
                ulang = False
                return saldo, pin
            case _:
                print("Input tidak valid, coba lagi")
        


file = open("data.txt", "r")

data = file.read()
data_baris = data.split("\n")
file.close()

rekening_input = input("Masukkan nomor rekening: ")

rekening_valid = False
pin_valid = False

for i, baris in enumerate(data_baris) :
    baris = baris.split("|")

    rekening = baris[0]
    pin = baris[1]
    nama = baris[2]
    saldo = int(baris[3])
    
    if rekening_input == rekening:
        rekening_valid = True
        
        while not pin_valid:
            pin_input = input("Masukkan PIN anda: ")
            if pin_input == pin:
                pin_valid = True
                print(f"Selamat datang {nama}")
                saldo, pin = menu_atm(saldo, pin)
                baris[1] = pin
                baris[3] = str(saldo)
                
                baris = "|".join(baris)
                data_baris[i] = baris
                
                data_baru = "\n".join(data_baris)
                
                file = open("data.txt", "w")
                file.write(data_baru)
                file.close()
            else:
                print("PIN salah coba lagi")
        break
    
    
if not rekening_valid:
    print(f"Error nomor rekening tidak ditemukan")
    
