# KAMUS
# salah : boolean
# id_peminjaman : integer
# tanggal_pengembalian : string
# gadget : integer
# gadget_return : array

def kembalikan(datas2, datas4, datas6): # F09-Mengembalikan Gadget
  for i in range(len(datas2)): # Print daftar gadget yang telah dipinjam dan belum dikembalikan
    for j in range (len(datas4)):
      if datas2[i][0] == datas4[j][2] and datas4[j][5] == "False":
        print(str(j+1) + ". " + str(datas2[i][1]))

  salah = True
  while salah: # Skema input ID peminjaman dan tanggal pengembalian
      id_peminjaman = int(input("Masukkan ID peminjaman: "))
      tanggal_pengembalian = input("Tanggal pengembalian: ")

      if id_peminjaman <= len(datas4):
          for i in range (len(datas4)):
            for j in range (len(datas2)):
              if datas4[i][0] == id_peminjaman and datas2[j][0] == datas4[i][2]: # Mencocokkan ID peminjaman dengan data yang ada
                  gadget = datas2[j][1]
                  salah = False # Item ada
                  datas2[j][3] = datas2[j][3] + datas4[i][4]
                  if datas6 == []:
                      id = 1
                  else:
                      id = datas6[-1][0] + 1
                  gadget_return = [id, id_peminjaman, tanggal_pengembalian]
                  datas6.append(gadget_return)
                  print("Item", gadget, "(x" + str(datas4[i][4]) + ") telah berhasil dikembalikan!")
                  datas4[i][5] = "True"
      if salah: # Item tidak ada
          print("Tidak ada item dengan ID tersebut!")
  return [datas2, datas4, datas6]