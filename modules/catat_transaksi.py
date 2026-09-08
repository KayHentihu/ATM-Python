def catat_transaksi(rekening, jenis, jumlah, rekening_tujuan=""):
    with open("data_transaksi.txt", "a") as file: 
        if rekening_tujuan:
            file.write(f"{rekening}|{jenis}|{jumlah}|{rekening_tujuan}\n")
        else:
            file.write(f"{rekening}|{jenis}|{jumlah}\n")