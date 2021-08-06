from FB01 import *  # import FB01.py untuk hashing

# KAMUS
# id_user :  integer
# username : string
# password : string
# input_username : string
# input_password : string 
# valid : boolean

def login(datas1): # F02-Login
    datas = datas1
    input_username = str(input("Masukan username: "))
    password = str(input("Masukan password: "))
    input_password = hashing(password) # menyocokkan kesamaan hasil hashing
    username = 2
    password = 3
    valid = False

    for i in range(len(datas1)):
        id_user = datas[i][0]

    # VERIFIKASI LOGIN TERHADAP DATA
    def login_verif(username, password, input_username, input_password, valid):
        for i in range(len(datas1)):
            adminORuser = datas[i][5]
            if (datas[i][username] == input_username) and (datas[i][password] == input_password):
                valid = True
                break
            else:
                valid = False
        if valid == False:
            print("Login gagal")
        else:
            print("Halo " + datas[i][5] + ": " + datas[i][1] + "! Selamat datang di Kantong Ajaib.")
        return [adminORuser,valid]

    loginverif = login_verif(username, password, input_username, input_password, valid)
    adminORuser = loginverif[0]
    valid = loginverif[1]
    return [id_user,username,adminORuser,valid]

