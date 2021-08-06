# KAMUS
# salah : boolean
# id_gadget : string
# tanggal : string
# jumlah : integer
# is_returned : string of boolean
# gadget_borrow : array

def pinjam(datas2, datas4, id_peminjam): # F08-Meminjam Gadget
  salah = True
  while salah: # Skema input ID item, tanggal, dan jumlah peminjaman
      id_gadget = input("Masukan ID item: ")
      tanggal = input("Tanggal peminjaman : ")
      jumlah = int(input("Jumlah peminjaman: "))
      is_returned = "False"

      if id_gadget[0] == "G": # Hanya dapat meminjam gadget
          for i in range (len(datas2)):
              if datas2[i][0] == id_gadget: # Mencocokkan ID item dengan data yang ada
                  salah = False # Item ada
                  while datas2[i][3] < jumlah:
                      print("Jumlah gadget tidak mencukupi")
                      print("Jumlah gadget yang tersedia adalah", datas2[i][3])
                      jumlah = int(input("Jumlah: "))
                  datas2[i][3] = datas2[i][3] - jumlah
                  if datas4 == []:
                      id_baru = 1
                  else:
                      id_baru = datas4[-1][0] + 1
                  gadget_borrow = [id_baru, id_peminjam, id_gadget, tanggal, jumlah, is_returned]
                  datas4.append(gadget_borrow)
                  print("Item", datas2[i][1], "(x" + str(jumlah) + ") telah berhasil dipinjam!")
      if salah: # Item tidak ada
          print("Tidak ada item dengan ID tersebut!")
  return [datas2,datas4]