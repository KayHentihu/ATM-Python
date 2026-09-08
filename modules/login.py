import os
from modules.pause import pause
from modules.menu_atm import menu_atm

def login(data_baris):
        
    rekening_valid = False

    while not rekening_valid:
        rekening_input = input("\nMasukkan nomor rekening: ")

        for i, baris in enumerate(data_baris):
            baris = baris.split("|")
            rekening = baris[0]

            if rekening_input == rekening:
                pin = baris[1]
                nama = baris[2]
                saldo = int(baris[3])
                rekening_valid = True
                pin_valid = False
                percobaan = 3

                while not pin_valid:
                    pin_input = input("\nMasukkan PIN anda: ")

                    if pin_input == pin:
                        pin_valid = True
                        os.system("cls")
                        saldo, pin = menu_atm(
                            saldo, pin, nama, rekening, data_baris
                        )

                        baris[1] = pin
                        baris[3] = str(saldo)
                        baris = "|".join(baris)
                        data_baris[i] = baris

                        data_baru = "\n".join(data_baris)

                        with open("data_nasabah.txt", "w") as file:
                            file.write(data_baru)
                            
                        return

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