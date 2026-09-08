from modules.login import login
     
with open("data_nasabah.txt", "r") as file:
    data = file.read()
    
data_baris = data.splitlines()

login(data_baris)