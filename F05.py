# KAMUS
# input_id : string
# isUnikID : boolean
# isValidID : boolean
# new_item_id : string
# new_item_nama : string
# new_item_deskripsi : string
# new_item_jumlah : string
# new_item_rarity : string
# new_item : array

def tambahitem(datas2,datas3): # F05-Menambah item

  input_id = input("Masukan ID: ")

  # INISIALISASI INPUT GADGET/CONSUMABLE TERHADAP DATA
  if input_id[0] == "G":
    datas = datas2

  elif input_id[0] == "C":
    datas = datas3

  else:
    print("Gagal menambahkan item karena ID tidak valid.")
    exit()

  new_items = []
  isUnikID = True
  isValidID = True

  while (input_id[0] != "G") and (input_id[0] != "C"): # Mengecek validitas ID
    isValidID = False
  else:
    isValidID = True

  # VALIDASI ID UNIK
  for i in range(len(datas)):
    if (input_id == datas[i][0]):
      isUnikID = False
    else:
      isUnikID = True 

  # PROSES TAMBAH ITEM
  if (isUnikID == True) and (isValidID == True):
    new_item_id = input_id
    new_item_nama = input("Masukan Nama: ")
    new_item_deskripsi = input("Masukan Deskripsi: ")
    new_item_jumlah = int(input("Masukan Jumlah: "))
    new_item_rarity = input("Masukan rarity: ")
    # JIKA INPUT RARITY SELAIN C, B, A, S
    while new_item_rarity != "C" and new_item_rarity != "B" and new_item_rarity != "S" and new_item_rarity != "A":
      print("Input rarity tidak valid!")
      new_item_rarity = input("Masukan rarity yang sesuai: ")
    # PENAMBAHAN ITEM BARU KE DATA
    if input_id[0] == "C":
      new_item_tahun = ""
      new_item = [new_item_id, new_item_nama, new_item_deskripsi, new_item_jumlah, new_item_rarity]
    else:
      new_item_tahun = int(input("Masukan tahun ditemukan: ")) 
      new_item = [new_item_id, new_item_nama, new_item_deskripsi, new_item_jumlah, new_item_rarity, new_item_tahun]
    new_items.append(new_item)
    datas += new_items
    print("Item telah berhasil ditambahkan ke database")

  else:
    print("Gagal menambahkan item karena ID sudah ada. Masukan ID lain selain ID berikut: ")
    for i in range(len(datas)):
      print(datas[i][0] + ". ", end="")
    print("")

  if input_id[0] == "G":
    return [datas, datas3]
    
  elif input_id[0] == "C":
    return [datas2, datas]