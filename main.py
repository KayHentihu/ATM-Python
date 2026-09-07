import os

def pause():
    input("\nTekan ENTER untuk melanjutkan...")
    os.system("cls")
    
def cek_saldo(saldo):
    print("\n===== CEK SALDO =====")
    print(f"\nSaldo anda: Rp.{saldo}")

def setor_tunai(saldo):
    print("\n===== SETOR TUNAI =====")
    
    try:
        jumlah = int(input("\nMasukkan jumlah setor: "))
        if jumlah > 0:
            saldo += jumlah
            print("\nSetor tunai berhasil!")
            print(f"\nSaldo baru : Rp.{saldo}")
            return saldo
        else:
            print("\nTidak dapat melakukan setor!")
    except ValueError:
        print("\nInput harus berupa angka")
        
    return saldo

def tarik_tunai(saldo):
    print("\n===== TARIK TUNAI =====")
    
    try:
        tarik = int(input("\nMasukkan jumlah tarik: "))
        if tarik > saldo:
            print("\nSaldo tidak mencukupi!")
        elif tarik <= 0:
            print("\nTidak dapat melakukan penarikan!")
        else:
            saldo -= tarik
            print("\nTarik tunai berhasil!")
            print(f"Saldo baru: Rp.{saldo}")
    except ValueError:
        print("\nInput harus berupa angka")
            
    return saldo
    
def ganti_pin(pin):
    print("\n===== GANTI PIN =====")
    pin_baru = input("\nMasukkan PIN baru: ")
    
    if len(pin_baru) != 4:    
        print("\nPIN harus terdiri dari 4 digit!")
    elif not pin_baru.isdigit():
        print("\nPIN harus berupa angka!")
    else:
        print("PIN baru berhasil disimpan!!")
        pin = pin_baru 
        
    return pin
    
    
def transfer(rekening, saldo, data_baris):
    print("\n===== TRANSFER =====")
    rekening_tujuan = input("\nMasukkan rekening tujuan: ")
    
    if rekening == rekening_tujuan:
        print("\nTidak dapat melakukan transfer ke rekening sendiri")
        return saldo
    
    rekening_ditemukan = False
    
    for i, baris in enumerate(data_baris):
        baris = baris.split("|")
        rekening_penerima = baris[0]
        
        if rekening_tujuan == rekening_penerima:
            print("\nRekening ditemukan!")
            rekening_ditemukan = True
            
            saldo_penerima = int(baris[3])
            
            try:
                jumlah_transfer = int(input("Masukkan jumlah transfer: "))
            except ValueError:
                print("\nInput harus berupa angka!")
                return saldo
                
            if jumlah_transfer > saldo:
                print("\nMaaf saldo tidak cukup!")
            elif jumlah_transfer <= 0:
                print("\nJumlah transfer harus lebih dari 0!")
            else:
                saldo -= jumlah_transfer
                saldo_penerima += jumlah_transfer
                baris[3] = str(saldo_penerima)
                data_baris[i] = "|".join(baris)
                
                print(f"\nBerhasil transfer RP.{jumlah_transfer} ke Norek: {rekening_penerima}")
            
    if not rekening_ditemukan:
        print("\nRekening tujuan tidak ditemukan!")            
        
    return saldo
                
    
    
def menu_atm(saldo, pin, nama,rekening, data_baris):
    ulang = True
    
    while ulang:
        print(f"\nSelamat datang {nama}!")
        print("Silahkan pilih transaksi\n")
        
        print("+====================+")
        print("|         ATM        |")
        print("+====================+")
        print("| 1. Cek Saldo       |")
        print("| 2. Setor Tunai     |")
        print("| 3. Tarik Tunai     |")
        print("| 4. Ganti PIN       |")
        print("| 5. Transfer        |")
        print("| 0. Keluar          |")
        print("+--------------------+")
        
        pilih = input("Pilih menu (0-5): ")
        
        match pilih:
            case "1":
                cek_saldo(saldo)
                pause()
            case "2":
                saldo = setor_tunai(saldo)
                pause()
            case "3":
                saldo = tarik_tunai(saldo)
                pause()
            case "4":
                pin = ganti_pin(pin)
                pause()
            case "5":
                saldo = transfer(rekening, saldo, data_baris)
                pause()
            case "0":
                print("Program selesai, Terima kasih!!!")
                ulang = False
                return saldo, pin
            case _:
                print("Input tidak valid, coba lagi")
                pause()
        
    

file = open("data.txt", "r")

data = file.read()
data_baris = data.split("\n")
file.close()

rekening_valid = False
pin_valid = False

while not rekening_valid:
    rekening_input = input("\nMasukkan nomor rekening: ")

    for i, baris in enumerate(data_baris) :
        baris = baris.split("|")

        rekening = baris[0]
        pin = baris[1]
        nama = baris[2]
        saldo = int(baris[3])
        
        if rekening_input == rekening:
            rekening_valid = True
            
            percobaan = 3
            while not pin_valid:
                pin_input = input("\nMasukkan PIN anda: ")
                if pin_input == pin:
                    pin_valid = True
                    os.system("cls")
                    saldo, pin = menu_atm(saldo, pin, nama, rekening, data_baris)
                    baris[1] = pin
                    baris[3] = str(saldo)
                    
                    baris = "|".join(baris)
                    data_baris[i] = baris
                    
                    data_baru = "\n".join(data_baris)
                    
                    file = open("data.txt", "w")
                    file.write(data_baru)
                    file.close()
                else:
                    percobaan -= 1
                    
                    if percobaan == 0:
                        print("\nMAAF PROGRAM DIHENTIKAN PAKSA!!")
                        break
                    else:
                        print("\nPIN salah coba lagi")
                        print(f"Sisa {percobaan} percobaan!!")
            break
    if not rekening_valid:
        print("\nError nomor rekening tidak ditemukan")
        pause()
    
    
    
