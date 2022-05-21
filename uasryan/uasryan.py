import os
Nama_Peserta = "ryan"
Nama_Paket = "01"
Fasilitas_Tambahan = "B"
Total_Bayar = 1000000
# Store Data
data = f" {Nama_Peserta} / {Nama_Paket} / {Fasilitas_Tambahan} / {format(Total_Bayar, ',')} ]"
with open("uasryan/Uas.txt", "a") as file:
    file.write(str(data) + "\n")
file.close()


def menu():
    menu = 5
    while True:
        try:
            print('''
|          PD. Travekar         |
|_______________________________|
|1| Tambah Peserta Transaksi    |
|-|-----------------------------|
|2| Lihat Peserta               |
|-|-----------------------------|
|3| Cari Peserta                |
|-|-----------------------------|
|4| Keluar Program              |
|-|-----------------------------| \n''')

            pilih = int(input("Pilih Menu : "))
            if pilih > menu or pilih < 1:
                print("Menu Tidak Ada")
                continue

            # Metode Dictionary
            selecting = {
                1: Tambah_Peserta,
                5: exit
            }
            # Metode get() untuk mengambil nilai dari dictionary
            return selecting.get(int(pilih))()
        except ValueError:
            print("\n! Inputan Harus Berupa Angka ! \n")
            continue


def Tambah_Peserta():
    kode = ["01", "02", "03", "04"]
    rute = ["Karawang - Pantai Pakis Jaya", "Karawang - Curug Cigentis - Gunung Sanggabuana",
            "Karawang - Candi Jiwa", "Karawang - Pantai"]
    tarif_paket = [1_000_000, 500_000, 600_000, 850_000]
    Kode_Tambahan = ["A", "B", "C"]
    fasilitas = ["Penginapan", "Penjemputan", "Kuliner"]
    Tarif_Tambahan = [1000_000, 500_000, 600_000]

    os.system("cls")

    print("------------------------------------DAFTAR RUTE PERJALANAN--------------------------------------")
    print("| Kode Paket | Rute Pejalanan                                 | Minimum Peserta | Tarif        |")
    print("------------------------------------------------------------------------------------------------")
    print("| 01         | Karawang - Pantai Pakis jaya                   | 6 Orang         | Rp. 1000.000 |")
    print("| 02         | Karawang - Curug Cigentis - Gunung Sanggabuana | 6 Orang         | Rp.  500.000 |")
    print("| 03         | Karawang - Candi Jiwa                          | 6 Orang         | Rp.  600.000 |")
    print("| 04         | Karawang - Pantai Samudra                      | 6 Orang         | Rp.  850.000 |")
    print("------------------------------------------------------------------------------------------------")
    print("")
    Nama_Peserta = input("Nama Peserta : ")
    kode = input("Kode Paket : ")
    if kode == "01":

        tarif_rute = tarif_paket[0]
        print("Rute : ", rute[0])
        print("Tarif Paket : ", tarif_rute)
    elif kode == "02":
        tarif_rute = tarif_paket[1]
        print("Rute : ", rute[1])
        print("Tarif Paket : ", tarif_rute)
    elif kode == "03":
        tarif_rute = tarif_paket[2]
        print("Rute : ", rute[2])
        print("Tarif Paket : ", tarif_rute)
    elif kode == "04":
        tarif_rute = tarif_paket[3]
        print("Rute : ", rute[3])
        print("Tarif Paket : ", tarif_rute)

    print("-------------DAFTAR RUTE PERJALANAN--------------")
    print("| Kode Tambahan | Fasilitas      | Tarif        |")
    print("-------------------------------------------------")
    print("| A            | Penginapan     | Rp. 1000.000  |")
    print("| B            | Penjemputan    | Rp.  500.000  |")
    print("| C            | Kuliner        | Rp.  600.000  |")
    print("-------------------------------------------------")
    print("")
    Kode_Tambahan = input("Kode Tambahan : ")
    if Kode_Tambahan == "A":
        # tarif_tambah = tarif_tambahan[0]
        print("Fasilitas : ", fasilitas[0])
        print("Tarif Tambahan : ", Tarif_Tambahan[0]+tarif_rute)
    elif Kode_Tambahan == "B":
        print("Nama Peserta : ", Nama_Peserta)
        print("rute : ", rute)
        print("Tarif : ", tarif_rute)
        print("Fasilitas : ", fasilitas[1])
        print("Tarif Tambahan : ", Tarif_tambahan[1])
        print("Jumlah Bayar : ", jumlah_bayar)
    elif Kode_Tambahan == "C":
        print("Fasilitas : ", fasilitas[0])
        print("Tarif Tambahan : ", Tarif_Tambahan[0]+tarif_rute)

        jumlah_tarif = int(tarif_rute+Tarif_tambahan)
        ppn = jumlah_tarif * 0.11
        jumlah_bayar = jumlah_tarif + ppn
        print("Nama Peserta : ", Nama_Peserta)
        print("rute : ", rute)
        print("Tarif : ", tarif_rute)
        print("Fasilitas : ", fasilitas)
        print("Tarif Tambahan : ", Tarif_tambahan)
        print("Jumlah Bayar : ", jumlah_bayar)


if __name__ == "__main__":
    menu()
