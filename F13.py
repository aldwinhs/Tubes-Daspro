# KAMUS
# array_date : array
# datetime_object : array
# date_sorted : array
# datas_sorted : array
# data_by_date : array
# reverse : boolean
# state : string

def riwayatambil(datas5, header5): # F13 - Melihat riwayat pengambilan consumable
  array_date = []
  for i in range(len(datas5)):
    for j in range(4):
        if (j == 3):
            array_date.append(datas5[i][j])

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
  for i in range(len(datas5)):
    for j in range(len(datas5)):
        if date_sorted[i] == datas5[j][3]:
            datas_sorted.append(datas5[j])

  a = 0
  b = len(datas5)
  def output_sort(a, b, data_by_date): # Print data yang telah diurutkan berdasarkan tahun
    if (b-a) <= 5:
      for i in range(a,b):
          print('ID Pengambilan     :' + str(data_by_date[i][0]))
          print('Nama Pengambil     :' + str(data_by_date[i][1]))
          print('Nama Consumable    :' + str(data_by_date[i][2]))
          print('Tanggal Pengambilan:' + str(data_by_date[i][3]))
          print('Jumlah             :' + str(data_by_date[i][4]))
          print('')
    elif (b-a) > 5:
      a = 0
      b = 4
      for i in range(a,b):
          print('ID Pengambilan     :' + str(data_by_date[i][0]))
          print('Nama Pengambil     :' + str(data_by_date[i][1]))
          print('Nama Consumable    :' + str(data_by_date[i][2]))
          print('Tanggal Pengambilan:' + str(data_by_date[i][3]))
          print('Jumlah             :' + str(data_by_date[i][4]))
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
            print('ID Pengambilan     :' + str(datas_sorted[i][0]))
            print('Nama Pengambil     :' + str(datas_sorted[i][1]))
            print('Nama Consumable    :' + str(datas_sorted[i][2]))
            print('Tanggal Pengambilan:' + str(datas_sorted[i][3]))
            print('Jumlah             :' + str(datas_sorted[i][4]))
            print('')
          break
        else:
          a = 4
          b = 9
          for i in range(a,b):
            print('ID Pengambilan     :' + str(datas_sorted[i][0]))
            print('Nama Pengambil     :' + str(datas_sorted[i][1]))
            print('Nama Consumable    :' + str(datas_sorted[i][2]))
            print('Tanggal Pengambilan:' + str(datas_sorted[i][3]))
            print('Jumlah             :' + str(datas_sorted[i][4]))
            print('')
          break
    else:
      break