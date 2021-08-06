# F14 - Load Data
def load1(dir):
  dir = "./"+dir+"/user.csv"
  with open(dir, "r") as f1:
      raw_lines1 = f1.readlines()
  f1.close()

  lines1 = [raw_line.replace("\n", "") for raw_line in raw_lines1] # hapus spasi

  def convert_array_data_to_real_values1(array_data):
    arr_cpy = array_data[:]
    for i in range(5):    # ubah id ke integer           
      if(i == 0):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil.append(temp)
              temp = ""
          else:
              temp += words
      hasil.append(temp)
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  raw_header1 = lines1.pop(0)

  header1 = convert_line_to_data(raw_header1)

  datas1 = []

  for line in lines1:
    array_of_data = convert_line_to_data(line)
    real_values1 = convert_array_data_to_real_values1(array_of_data)
    datas1.append(real_values1)
  return [header1,datas1]
def load2(dir):
  dir = "./"+dir+"/gadget.csv"
  with open(dir, "r") as f2:
      raw_lines2 = f2.readlines()
  f2.close()

  lines2 = [raw_line.replace("\n", "") for raw_line in raw_lines2] # hapus spasi

  def convert_array_data_to_real_values2(array_data):
    arr_cpy = array_data[:]
    for i in range(5):    # ubah id ke integer           
      if(i == 3):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil.append(temp)
              temp = ""
          else:
              temp += words
      hasil.append(temp)
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  raw_header2 = lines2.pop(0)

  header2 = convert_line_to_data(raw_header2)

  datas2 = []

  for line in lines2:
    array_of_data = convert_line_to_data(line)
    real_values2 = convert_array_data_to_real_values2(array_of_data)
    datas2.append(real_values2)
  return [header2,datas2]

def load3(dir):
  dir = "./"+dir+"/consumable.csv"
  with open(dir, "r") as f3:
      raw_lines3 = f3.readlines()
  f3.close()

  lines3 = [raw_line.replace("\n", "") for raw_line in raw_lines3] # hapus spasi

  def convert_array_data_to_real_values3(array_data):
    arr_cpy = array_data[:]
    for i in range(4):    # ubah id ke integer           
      if(i == 3): # kolom id
        arr_cpy[i] = int(arr_cpy[i])
      # elif(i == 3): # kolom jumlah
      #   arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil.append(temp)
              temp = ""
          else:
              temp += words
      hasil.append(temp)
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  raw_header3 = lines3.pop(0)

  header3 = convert_line_to_data(raw_header3)

  datas3 = []

  for line in lines3:
    array_of_data = convert_line_to_data(line)
    real_values3 = convert_array_data_to_real_values3(array_of_data)
    datas3.append(real_values3)
  return [header3,datas3]
  
def load4(dir):
  dir = "./"+dir+"/gadget_borrow_history.csv"
  with open(dir, "r") as f4:
      raw_lines4 = f4.readlines()
  f4.close()

  lines4 = [raw_line.replace("\n", "") for raw_line in raw_lines4] # hapus spasi

  def convert_array_data_to_real_values4(array_data):
    arr_cpy = array_data[:]
    for i in range(5):    # ubah id ke integer           
      if(i == 0):
        arr_cpy[i] = int(arr_cpy[i])
      elif(i == 4):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil.append(temp)
              temp = ""
          else:
              temp += words
      hasil.append(temp)
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  raw_header4 = lines4.pop(0)

  header4 = convert_line_to_data(raw_header4)

  datas4 = []

  for line in lines4:
    array_of_data = convert_line_to_data(line)
    real_values4 = convert_array_data_to_real_values4(array_of_data)
    datas4.append(real_values4)
  return [header4,datas4]

def load5(dir):
  dir = "./"+dir+"/consumable_history.csv"
  with open(dir, "r") as f5:
      raw_lines5 = f5.readlines()
  f5.close()

  lines5 = [raw_line.replace("\n", "") for raw_line in raw_lines5] # hapus spasi

  def convert_array_data_to_real_values5(array_data):
    arr_cpy = array_data[:]
    for i in range(4):
      if(i == 4):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil.append(temp)
              temp = ""
          else:
              temp += words
      hasil.append(temp)
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  raw_header5 = lines5.pop(0)

  header5 = convert_line_to_data(raw_header5)

  datas5 = []

  for line in lines5:
    array_of_data = convert_line_to_data(line)
    real_values5 = convert_array_data_to_real_values5(array_of_data)
    datas5.append(real_values5)
  return [header5,datas5]

def load6(dir):
  dir = "./"+dir+"/gadget_return_history.csv"
  with open(dir, "r") as f6:
      raw_lines6 = f6.readlines()
  f6.close()

  lines6 = [raw_line.replace("\n", "") for raw_line in raw_lines6] # hapus spasi

  def convert_array_data_to_real_values6(array_data):
    arr_cpy = array_data[:]
    for i in range(2):    # ubah id ke integer           
      if(i == 0):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

  def split(x, delimitter):
      hasil = []
      temp = ""
      for words in x:
          if words == delimitter:
              hasil.append(temp)
              temp = ""
          else:
              temp += words
      hasil.append(temp)
      return hasil

  def convert_line_to_data(line):
    raw_array_of_data = split(line,";") # ubah string jadi integer
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data
  raw_header6 = lines6.pop(0)

  header6 = convert_line_to_data(raw_header6)

  datas6 = []

  for line in lines6:
    array_of_data = convert_line_to_data(line)
    real_values6 = convert_array_data_to_real_values6(array_of_data)
    datas6.append(real_values6)
  return [header6,datas6]

## YANG HARUS DIDUPLIKASI
# fn, linesn, raw_linesn, raw_headern, real_valuesn, datasn, headern <-- VARIABLE
# n nya diganti angka, jadi misal mau nambahin csv baru namanya f3
# tambahin open("./Data/nama.csv", "r") as f3: di argumen with paling atas
# nanti copy setiap variable yg gue tulis di atas, dengan n = 3 karena kita namainnya f3