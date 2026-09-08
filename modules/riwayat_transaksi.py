def riwayat_transaksi(rekening):
    print("\n===== RIWAYAT TRANSAKSI =====")
    
    with open("data_transaksi.txt", "r") as file:
           
        data = file.readlines()
        
    for baris in data:
        transaksi = baris.strip().split("|")
        
        if transaksi[0] == rekening:
            print(baris.strip())
