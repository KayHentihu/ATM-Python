from modules.pause import pause
from modules.cek_saldo import cek_saldo
from modules.setor_tunai import setor_tunai
from modules.tarik_tunai import tarik_tunai
from modules.ganti_pin import ganti_pin
from modules.transfer import transfer
from modules.riwayat_transaksi import riwayat_transaksi



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
        print("| 6. Riwayat         |")
        print("| 0. Keluar          |")
        print("+--------------------+")
        
        pilih = input("Pilih menu (0-6): ")
        
        match pilih:
            case "1":
                cek_saldo(saldo)
                pause()
            case "2":
                saldo = setor_tunai(saldo, rekening)
                pause()
            case "3":
                saldo = tarik_tunai(saldo, rekening)
                pause()
            case "4":
                pin = ganti_pin(pin)
                pause()
            case "5":
                saldo = transfer(rekening, saldo, data_baris)
                pause()
            case "6":
                riwayat_transaksi(rekening)
                pause()
            case "0":
                print("Program selesai, Terima kasih!!!")
                ulang = False
                return saldo, pin
            case _:
                print("Input tidak valid, coba lagi")
                pause()
 