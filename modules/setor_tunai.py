from modules.catat_transaksi import catat_transaksi

def setor_tunai(saldo, rekening):
    print("\n===== SETOR TUNAI =====")
    
    try:
        jumlah = int(input("\nMasukkan jumlah setor: "))
        if jumlah > 0:
            saldo += jumlah
            
            catat_transaksi(rekening, "SETOR", jumlah)
            
            print("\nSetor tunai berhasil!")
            print(f"\nSaldo baru : Rp.{saldo}")
            
            return saldo
        else:
            print("\nTidak dapat melakukan setor!")
    except ValueError:
        print("\nInput harus berupa angka")
        
    return saldo
