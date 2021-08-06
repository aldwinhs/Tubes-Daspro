# KAMUS
# input_rarity :  string
# jumlah : integer

def carirarity(datas2): # F03-Pencarian Gadget berdasarkan Rarity
  rarity = 4
  input_rarity = input("Masukkan rarity: ")

  def findRarity(rarity, input_rarity):
      jumlah = 0
      print("")
      print("Hasil pencarian: ")
      print("")
      # PENCARIAN RARITY DALAM ARRAY
      for i in range(len(datas2)):
          if (datas2[i][rarity] == input_rarity): # jenis input pasti valid (C,B,A,S)
            jumlah += 1
            print("Nama            : ", datas2[i][1])
            print("Deskripsi       : ", datas2[i][2])
            print("Jumlah          : ", datas2[i][3])
            print("Rarity          : ", datas2[i][4])
            print("Tahun Ditemukan : ", datas2[i][5])
            print("")
      if jumlah == 0:
        print("Tidak ada gadget yang ditemukan")

  findRarity(rarity, input_rarity)
