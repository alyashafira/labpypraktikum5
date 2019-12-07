# Membuat dictionary

print (" PROGRAM INPUT NILAI AKHIR MAHASISWA ")
print ("======================================")

data={}
while True:
    print("")
    a=input("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar: ")  # Untuk Menampilkan Menu Pilihan
    if a.lower() == "k":                            # lower() adalah metode bawaan yang digunakan untuk penanganan string, dan variabel "K" difungsikan untuk menu pilihan keluar
        break                                       # break untuk berhenti
    elif a.lower() == "l":                          # Untuk menampilkan tabel
        print ("++++++++++++++++++++++++++DATA NILAI AKHIR MAHASISWA++++++++++++++++++++++++++++")
        print ("")
        print ("===============================================================================")
        print ("===============================================================================")
        print ("| NO |    NAMA     |     NIM     |   TUGAS   |   UTS   |   UAS   |    AKHIR   |")
        print ("===============================================================================")
        print ("===============================================================================")
        i=0
        for x in data.items():
            i+=1
            print ("| {6:1}  |  {0:9s}  |  {1:9s}  |  {2:6d}  |  {3:6d}  |  {4:5d}   |  {5:9.2f} |"
                   .format (x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i ))
            print("===============================================================================")
    elif a.lower() == "t":       # Untuk menambahkan data mahasiswa berupa ("nama, nim, ntugas, nuts, nuas, dan menghitung nilai akhir yg diinput
        print (" Tambah Data Mahasiswa ")
        print ("=======================")
        NM = input("Nama Mahasiswa :")
        NIM = input("NIM            :")
        NTUGAS = int(input("Nilai Tugas    :"))
        NUTS = int(input("Nilai UTS      :"))
        NUAS = int(input("Nilai UAS      :"))
        nilai = ((NTUGAS)*30/100 + (NUTS)*35/ 100 + (NUAS)*35/100)          # cara menghitung nilai akhir
        data[NM] = NIM, NTUGAS, NUTS, NUAS, nilai
    elif a.lower() == "u":
        print (" Ubah Data Mahasiswa ")
        print ("=====================")
        NM = input("Nama Mahasiswa :")
        if NM in data.keys():
            NIM = input("NIM            :")
            NTUGAS = int(input("Nilai Tugas    :"))
            NUTS = int(input("Nilai UTS    :"))
            NUAS = int(input("Nilai UAS    :"))
        else:
            print ("data {0} tidak ada".format(NM))
    elif a.lower() =='h':
        print (" Hapus Data Mahasiswa ")
        print ("======================")
        NM = input("Nama Mahasiswa :")
        if NM in data.keys():
            del data[NM]
        else:
            print ("data {0} tidak ada".format(NM))
    elif a.lower() == "c":
        print (" Cari Data Mahasiswa ")
        print ("=====================")
        NM = input("Nama Mahasiswa:")
        if NM in data.keys():
            print(" Hasil Pencarian Data Mahasiswa")
            print ("===============================================================================")
            print(" Data Nilai Mahasiswa {0} adalah {1}"
                  .format(NM, data[NM]))
        else:
            print ("data{0} tidak ada".format(NM))
    else:
        print (" Pilihlah Menu Yang Tersedia ")