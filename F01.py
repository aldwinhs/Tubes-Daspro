from FB01 import *

# KAMUS
# new_user_idx :  integer
# new_user_name : string
# new_user_username : string 
# password : string
# new_user_password : string
# new_user_alamat : string
# new_user_role : string
# new_user : array

def register(datas1,header1,dir):
  # INISIALISASI NEW USER
  new_users = []
  isUnik = False
  new_user_idx = datas1[-1][0] + 1 # PENAMBAHAN DATA PADA ELEMEN TERAKHIR

  new_user_name = input("Masukan nama: ")
  new_user_username = input("Masukan username: ")
  # VALIDASI TIDAK DAPAT MEMBUAT AKUN ADMIN
  if new_user_username == "admin":
    print("Tidak bisa membuat admin, coba username lain.")
    exit()
  while isUnik == False: # membaca keunikan username
    for i in range(len(datas1)):
      if (datas1[i][2] != new_user_username) or new_user_username == " " or new_user_username.isspace():
        isUnik = True
      else:
        isUnik = False
        new_user_username = input("Username harus unik, masukan username lain: ")

  password = input("Masukkan password: ")
  new_user_password = hashing(password) # melakukan hashing password yang telah diinput
  new_user_alamat = input("Masukan alamat: ")
  print("")
  # PENAMBAHAN USER KE DALAM DATA
  new_user_role = "user"
  new_user = [new_user_idx, new_user_name, new_user_username, new_user_password, new_user_alamat, new_user_role]
  new_users.append(new_user)

  datas1 += new_users

  print("User", new_user_username, "telah berhasil register ke dalam Kantong Ajaib")

  def convert_datas_to_string(header,datas):
    string_data = ";".join(header) + "\n"
    for arr_data in datas:
      arr_data_all_string = [str(var) for var in arr_data]
      string_data += ";".join(arr_data_all_string)
      string_data += "\n"
    return string_data

  # AUTOSAVE DATA USER PADA USER.CSV
  datas_as_string = convert_datas_to_string(header1,datas1)
  f1 = open("./"+dir+"/user.csv", "w")
  f1.write(datas_as_string)
  f1.close()
  return datas1