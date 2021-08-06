# KAMUS
# id_hapus : string
# ketemu : boolean
# nama : integer
# ID : integer
# persetujuan : string

def hapusitem(datas2, datas3): ## F06-Menghapus Gadget atau Consumable
    ## PROGRAM
    ketemu = False
    while not(ketemu): 
        id_hapus= input("Masukan ID Item: ")
        nama = 1
        ID = 0


        if id_hapus[0] == "G" or id_hapus[0] == "C": ## Mengecek apakah item gadget atau consumable
            if id_hapus[0] == "G":

                ##PROGRAM
                for i in range(len(datas2)):
                    if (str(datas2[i][ID])) == id_hapus:
                        ketemu = True
                        persetujuan = input("Apakah anda ingin menghapus "+(datas2[i][nama])+" (Y/N)? ")
                        while not(persetujuan == "Y" or persetujuan == "N"):
                            print("Masukan tidak sesuai.")
                            persetujuan = input("Apakah anda ingin menghapus "+(datas2[i][nama])+" (Y/N)? ")
                        if persetujuan == "Y":
                            datas2.pop(i)
                            print("Item telah berhasil dihapus dari database.")
                            break
                        elif persetujuan == "N":
                            print("Item tidak dihapus")
                            break
                if not(ketemu):
                    print("Tidak ada item dengan ID tersebut")

            else: #id_hapus == "C"

                ##PROGRAM
                for i in range(len(datas3)):
                    if (str(datas3[i][ID])) == id_hapus:
                        ketemu = True
                        persetujuan = input("Apakah anda ingin menghapus "+ (datas3[i][nama])+ " (Y/N)? ")
                        while not(persetujuan == "Y" or persetujuan == "N"):
                            print("Masukan tidak sesuai.")
                            persetujuan = input("Apakah anda ingin menghapus "+(datas3[i][nama])+" (Y/N)? ")
                        if persetujuan == "Y":
                            datas3.pop(i)
                            print("Item telah berhasil dihapus dari database.")
                            break
                        elif persetujuan == "N":
                            print("item tidak dihapus")
                            break
                if not(ketemu):
                    print("Tidak ada item dengan ID tersebut")
        else:
            print("Tidak ada item dengan ID tersebut")
    return [datas2, datas3]