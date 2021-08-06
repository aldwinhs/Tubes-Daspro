# KAMUS
# salah : boolean
# id_minta : string
# banyak_minta : integer
# tanggal_minta : string
# id_baru : integer
# id_pengguna : integer
# data_baru : array

def minta(datas3,datas5,id_pengguna): ## F08-Meminta Consumable
  salah = True
  ##INPUT
  while salah:
      id_minta = input("Masukan ID item: ")
      banyak_minta = int(input("Jumlah: "))
      tanggal_minta = input("Tanggal permintaan: ")

      if id_minta[0] == "C": ##ID UNTUK MEMINTA CONSUMABLES YANG VALID
          for i in range (len(datas3)):
              if datas3[i][0] == id_minta: ##MENGECEK APABILA ADA ID YANG SESUAI
                  salah = False
                  while datas3[i][3] < banyak_minta: #Meminta user untuk menginput sesuai banyaknya consumables
                      print("Jumlah consumables tidak mencukupi")
                      print("Jumlah consumables yang tersedia adalah", datas3[i][3])
                      banyak_minta = int(input("Jumlah: "))
                  datas3[i][3] = datas3[i][3] - banyak_minta ##KURANGI CONSUMABLE DI DATAS
                  if datas5 == []:
                      id_baru = 1
                  else:
                      id_baru = datas5[-1][0] + 1
                  data_baru = [id_baru, id_pengguna, datas3[i][0], tanggal_minta, banyak_minta] #array dengan format id;id_pengambil;id_consumable;tanggal_pengambilan;jumlah
                  datas5.append(data_baru)
                  print("Item", datas3[i][1], "(x" + str(banyak_minta) + ") telah berhasil diambil!")
      if salah:
          print("Tidak ada item dengan ID tersebut!")
  return [datas3,datas5]