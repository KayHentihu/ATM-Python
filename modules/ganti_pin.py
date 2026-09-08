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
   