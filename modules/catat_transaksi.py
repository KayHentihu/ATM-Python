def catat_transaksi(rekening, jenis, jumlah, status, rekening_tujuan=""):
    with open("data_transaksi.txt", "a") as file: 
        if rekening_tujuan:
            file.write(f"{status}|{rekening}|{jenis}|{jumlah}|{rekening_tujuan}\n")
        else:
            file.write(f"{status}|{rekening}|{jenis}|{jumlah}\n")