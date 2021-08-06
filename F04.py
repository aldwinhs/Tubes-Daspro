# KAMUS
# nyaritahun : integer
# kategorinyari : string
# urut_tahun : array

def caritahun(datas2): ## F04-PENCARIAN GADGET BERDASARKAN TAHUN DITEMUKAN
    ## INPUT
    nyaritahun = int(input("Masukan tahun: "))
    kategorinyari = input("Masukkan kategori: ")
    tahun = 5 ##INDEKS CSV UNTUK KOLOM TAHUN
    jumlah = 0

    ##MENGURUTKAN TAHUN DARI YANG TERBESAR
    urut_tahun = [0 for i in range (len(datas2))]
    for i in range (len(datas2)):
        urut_tahun[i] = datas2[i]

    for i in range (len(urut_tahun)):
        imax = i
        for j in range (i+1, len(urut_tahun)):
            if (urut_tahun[imax][tahun] < urut_tahun[j][tahun]):
                imax = j
        tmp = urut_tahun[imax]
        urut_tahun[imax] = urut_tahun[i]
        urut_tahun[i] = tmp



    print("\nHasil Pencarian: \n")


    ##MELAKUKAN PENCARIAN TAHUN YANG SESUAI
    if kategorinyari == "=":
        for i in range(len(datas2)):
            if (int(urut_tahun[i][tahun]) == nyaritahun):
                jumlah += 1
                print("Nama:", urut_tahun[i][1])
                print("Deskripsi:", urut_tahun[i][2])
                print("Jumlah:", urut_tahun[i][3])
                print("Rarity:", urut_tahun[i][4])
                print("Tahun Ditemukan:", urut_tahun[i][5])
                print()

    elif kategorinyari == ">":
        for i in range(len(datas2)):
            if (int(urut_tahun[i][tahun]) > nyaritahun):
                jumlah += 1
                print("Nama:", urut_tahun[i][1])
                print("Deskripsi:", urut_tahun[i][2])
                print("Jumlah:", urut_tahun[i][3])
                print("Rarity:", urut_tahun[i][4])
                print("Tahun Ditemukan:", urut_tahun[i][5])
                print()

    elif kategorinyari == "<":
        for i in range(len(datas2)):
            if (int(urut_tahun[i][tahun]) < nyaritahun):
                jumlah += 1
                print("Nama:", urut_tahun[i][1])
                print("Deskripsi:", urut_tahun[i][2])
                print("Jumlah:", urut_tahun[i][3])
                print("Rarity:", urut_tahun[i][4])
                print("Tahun Ditemukan:", urut_tahun[i][5])
                print()

    elif kategorinyari == ">=":
        for i in range(len(datas2)):
            if (int(urut_tahun[i][tahun]) >= nyaritahun):
                jumlah += 1
                print("Nama:", urut_tahun[i][1])
                print("Deskripsi:", urut_tahun[i][2])
                print("Jumlah:", urut_tahun[i][3])
                print("Rarity:", urut_tahun[i][4])
                print("Tahun Ditemukan:", urut_tahun[i][5])
                print()
                
    else: #kategorinyari == "<=": (KARENA INPUT SELALU BENAR) 
        for i in range(len(datas2)):
            if (int(urut_tahun[i][tahun]) <= nyaritahun):
                jumlah += 1
                print("Nama:", urut_tahun[i][1])
                print("Deskripsi:", urut_tahun[i][2])
                print("Jumlah:", urut_tahun[i][3])
                print("Rarity:", urut_tahun[i][4])
                print("Tahun Ditemukan:", urut_tahun[i][5])
                print()

    if jumlah == 0:
        print("Tidak ada gadget yang ditemukan")
