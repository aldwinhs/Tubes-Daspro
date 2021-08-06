# KAMUS
# id_ubah : string
# ketemu : boolean
# nama : integer
# jumlah : integer
# banyakubah : integer

def ubahjumlah(datas2, datas3): # F07-Mengubah Jumlah Gadget atau Consumable pada Inventory
    ketemu = False
    while not(ketemu): 
        id_ubah= input("Masukan ID: ")
        ID = 0
        nama = 1
        jumlah = 3

        if id_ubah[0] == "G" or id_ubah[0] == "C": # Mengecek apakah item gadget atau consumable
            if id_ubah[0] == "G":

                for i in range(len(datas2)):
                    if (str(datas2[i][ID])) == id_ubah:
                        ketemu = True
                        cukup = False
                        while not(cukup):
                          banyakubah = int(input("Masukkan Jumlah: "))
                          if banyakubah < 0:
                            if (datas2[i][jumlah] + banyakubah) < 0:
                              print(-banyakubah, datas2[i][nama], "gagal dibuang karena stok kurang. Stok sekarang:", datas2[i][jumlah], "(< "+ str(banyakubah) +")")
                            else:
                              cukup = True
                              datas2[i][jumlah] = datas2[i][jumlah] + banyakubah
                              print(-banyakubah, datas2[i][nama], "berhasil dibuang. Stok sekarang:", datas2[i][jumlah])
                          else: #banyakubah >= 0
                            cukup = True
                            datas2[i][jumlah] = datas2[i][jumlah] + banyakubah
                            print(banyakubah, datas2[i][nama], "berhasil ditambahkan. Stok sekarang:", datas2[i][jumlah])
                if not(ketemu):
                    print("Tidak ada item dengan ID tersebut")

            else: # id_ubah == "C"

                for i in range(len(datas3)):
                    if (str(datas3[i][ID])) == id_ubah:
                        ketemu = True
                        cukup = False
                        while not(cukup):
                          banyakubah = int(input("Masukkan Jumlah: "))
                          if banyakubah < 0:
                            if (datas3[i][jumlah] + banyakubah) < 0:
                              print(-banyakubah, datas3[i][nama], "gagal dibuang karena stok kurang. Stok sekarang:", datas3[i][jumlah], "(< "+ str(banyakubah) +")")
                            else:
                              cukup = True
                              datas3[i][jumlah] = datas3[i][jumlah] + banyakubah
                              print(-banyakubah, datas3[i][nama], "berhasil dibuang. Stok sekarang:", datas3[i][jumlah])
                          else: #banyakubah >= 0
                            cukup = True
                            datas3[i][jumlah] = datas3[i][jumlah] + banyakubah
                            print(banyakubah, datas3[i][nama], "berhasil ditambahkan. Stok sekarang:", datas3[i][jumlah])
                if not(ketemu):
                    print("Tidak ada item dengan ID tersebut")
        else:
            print("Tidak ada item dengan ID tersebut")
    return [datas2, datas3]