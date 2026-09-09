from modules.catat_transaksi import catat_transaksi

def tarik_tunai(saldo, rekening):
    print("\n===== TARIK TUNAI =====")
    
    try:
        tarik = int(input("\nMasukkan jumlah tarik: "))
        if tarik > saldo:
            print("\nSaldo tidak mencukupi!")
        elif tarik <= 0:
            print("\nTidak dapat melakukan penarikan!")
        else:
            saldo -= tarik
            
            catat_transaksi("KELUAR", rekening, "TARIK", tarik)
            
            print("\nTarik tunai berhasil!")
            print(f"Saldo baru: Rp.{saldo}")
    except ValueError:
        print("\nInput harus berupa angka")
            
    return saldo
 