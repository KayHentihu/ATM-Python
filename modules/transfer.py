from modules.catat_transaksi import catat_transaksi    

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
                catat_transaksi(rekening, "TRANSFER", jumlah_transfer, rekening_tujuan)
                
                print(f"\nBerhasil transfer RP.{jumlah_transfer} ke Norek: {rekening_penerima}")
            
            break
            
    if not rekening_ditemukan:
        print("\nRekening tujuan tidak ditemukan!")            
        
    return saldo
 