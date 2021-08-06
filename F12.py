# KAMUS
# array_date : array
# datetime_object : array
# date_sorted : array
# datas_sorted : array
# data_by_date : array
# reverse : boolean
# state : string

def riwayatkembali(datas4, header4): # F12 - Melihat riwayat pengembalian gadget
  array_date = []
  for i in range(len(datas4)):
    for j in range(5):
        if (j == 3):
            array_date.append(datas4[i][j])

  from datetime import datetime
  datetime_object = []
  # Sorting data berdasarkan tahun
  for i in range(len(array_date)):
    datetime_var = datetime.strptime(array_date[i], '%d/%m/%Y')
    datetime_object.append(datetime_var)
  datetime_sorted = sorted(datetime_object, reverse=True)

  date_sorted = []
  for i in range(len(datetime_sorted)):
    date_var = datetime.strftime(datetime_sorted[i], '%d/%m/%Y')
    date_sorted.append(date_var)

  datas_sorted = []
  for i in range(len(datas4)):
    for j in range(len(datas4)):
        if date_sorted[i] == datas4[j][3]:
            datas_sorted.append(datas4[j])
  
  a = 0
  b = len(datas4)
  def output_sort(a, b, data_by_date): # Print data yang telah diurutkan berdasarkan tahun
    if (b-a) <= 4:
      for i in range(a,b):
        if data_by_date[i][5] == "True":
          print('ID Peminjaman     :' + str(data_by_date[i][0]))
          print('Nama Pengambil    :' + str(data_by_date[i][1]))
          print('Nama Gadget       :' + str(data_by_date[i][2]))
          print('Tanggal Peminjaman:' + str(data_by_date[i][3]))
          print('')
    elif (b-a) > 4:
      a = 0
      b = 4
      for i in range(a,b):
        if data_by_date[i][5] == "True":
          print('ID Peminjaman     :' + str(data_by_date[i][0]))
          print('Nama Pengambil    :' + str(data_by_date[i][1]))
          print('Nama Gadget       :' + str(data_by_date[i][2]))
          print('Tanggal Peminjaman:' + str(data_by_date[i][3]))
          print('')
    return('')

  print(output_sort(a, b, datas_sorted))

  while True:
    if len(datas_sorted) > 4:
      state = input('Lihat riwayat sebelumnya? (yes/no) ')
      if state == 'yes':
        if len(datas_sorted) < 9:
          a = 4
          b = len(datas_sorted)
          for i in range(a,b):
            print('ID Peminjaman     :' + str(datas_sorted[i][0]))
            print('Nama Pengambil    :' + str(datas_sorted[i][1]))
            print('Nama Gadget       :' + str(datas_sorted[i][2]))
            print('Tanggal Peminjaman:' + str(datas_sorted[i][3]))
            print('')
          break
        else:
          a = 4
          b = 9
          for i in range(a,b):
            print('ID Peminjaman     :' + str(datas_sorted[i][0]))
            print('Nama Pengambil    :' + str(datas_sorted[i][1]))
            print('Nama Gadget       :' + str(datas_sorted[i][2]))
            print('Tanggal Peminjaman:' + str(datas_sorted[i][3]))
            print('')
          break
    else:
      break