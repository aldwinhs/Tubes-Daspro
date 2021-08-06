# AKUN ADMIN
# username : admin
# password : password

import argparse
import os
import sys
from F01 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *
# F17 langsung diimplementasikan dalam program ini

# Create the parser
my_parser = argparse.ArgumentParser(description="Melihat folder penyimpanan ada")

# Add the arguments
my_parser.add_argument("Path", metavar="nama_folder", type=str, help='the folder to be loaded')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("Tidak ada nama folder yang diberikan!")
    print("python kantongajaib.py <nama_folder>")
    sys.exit()

##PROGRAM UTAMA
load1 = load1(input_path)
load2 = load2(input_path)
load3 = load3(input_path)
load4 = load4(input_path)
load5 = load5(input_path)
load6 = load6(input_path)
header1 = load1[0]
header2 = load2[0]
header3 = load3[0]
header4 = load4[0]
header5 = load5[0]
header6 = load6[0]
datas1 = load1[1]
datas2 = load2[1]
datas3 = load3[1]
datas4 = load4[1]
datas5 = load5[1]
datas6 = load6[1]


print("Selamat datang di kantong ajaib!")
valid = False
while not(valid):  
    command = input(">> ")
    while not(command == "login" or command == "exit" or command == "help"):
        print ("Silahkan register atau login terlebih dahulu")
        command = input(">> ")
    if (command == "help"): #F16
        adminORuser = ""
        help(adminORuser)
        command = input(">> ")
    if (command == "login"): #F02
        loginuser = login(datas1)
        id_user = loginuser[0]
        username = loginuser[1]
        adminORuser = loginuser[2]
        valid = loginuser[3]
    else: #exit
        print("Sampai jumpa")
        exit()

command = input(">> ")
while True:
    if (command == "register" and adminORuser == "admin"): #F01
        datas1 = register(datas1,header1,input_path)
        command = input(">> ")
    if (command == "carirarity" and (adminORuser == "admin" or adminORuser == "user")): #F03
        carirarity(datas2)
        command = input(">> ")
    elif (command == "caritahun" and (adminORuser == "admin" or adminORuser == "user")): #F04
        caritahun(datas2)
        command = input(">> ")
    elif (command == "tambahitem" and adminORuser == "admin"): #F05
        itemadd = tambahitem(datas2,datas3)
        datas2 = itemadd[0]
        datas3 = itemadd[1]
        command = input(">> ")
    elif (command == "hapusitem"  and adminORuser == "admin"): #F06
        itemhapus = hapusitem(datas2, datas3)
        datas2 = itemhapus[0]
        datas3 = itemhapus[1]
        command = input(">> ")
    elif (command == "ubahjumlah"  and adminORuser == "admin"): #F07
        jumlahubah = ubahjumlah(datas2, datas3)
        datas2 = jumlahubah[0]
        datas3 = jumlahubah[1]
        command = input(">> ")
    elif (command == "pinjam" and adminORuser == "user"): #F08
        borrow = pinjam(datas2, datas4, id_user)
        datas2 = borrow[0]
        datas4 = borrow[1]
        command = input(">> ")
    elif (command == "kembalikan" and adminORuser == "user"): #F09
        returngadget = kembalikan(datas2, datas4, datas6)
        datas2 = returngadget[0]
        datas4 = returngadget[1]
        datas6 = returngadget[2]
        command = input(">> ")
    elif (command == "minta" and adminORuser == "user"): #F10
        askitem = minta(datas3,datas5,username)
        datas3 = askitem[0]
        datas5 = askitem[1]
        command = input(">> ")
    elif (command == "riwayatpinjam" and adminORuser == "admin"): #F11
        riwayatpinjam(datas4, header4)
        command = input(">> ")
    elif (command == "riwayatkembali" and adminORuser == "admin"): #F12
        riwayatkembali(datas4, header4)
        command = input(">> ")
    elif (command == "riwayatambil" and adminORuser == "admin"): #F13
        riwayatambil(datas5, header5)
        command = input(">> ")
    elif (command == "save" and (adminORuser == "admin" or adminORuser == "user")): #F15
        dir = input("Masukkan nama folder penyimpanan: ")
        save(dir,datas1,header1,'user.csv')
        save(dir,datas2,header2,'gadget.csv')
        save(dir,datas3,header3,'consumable.csv')
        save(dir,datas4,header4,'gadget_borrow_history.csv')
        save(dir,datas5,header5,'consumable_history.csv')
        save(dir,datas6,header6,'gadget_return_history.csv')
        print("Saving...")
        print("Data telah disimpan pada folder", dir, "!")
        command = input(">> ")
    elif (command == "help" and (adminORuser == "admin" or adminORuser == "user")): #F16
        help(adminORuser)
        command = input(">> ")
    elif (command == "exit"): #F17
        print('Apakah Anda mau melakukan penyimpanan file yang telah diubah? (yes/no)')
        command = input('>> ')
        if command == 'yes':
            dir = input("Masukkan nama folder penyimpanan: ")
            save(dir,datas1,header1,'user.csv')
            save(dir,datas2,header2,'gadget.csv')
            save(dir,datas3,header3,'consumable.csv')
            save(dir,datas4,header4,'gadget_borrow_history.csv')
            save(dir,datas5,header5,'consumable_history.csv')
            save(dir,datas6,header6,'gadget_return_history.csv')
            print("Saving...")
            print("Data telah disimpan pada folder", dir, "!")
            print('Sampai jumpa')
            exit()
        elif command =='no':
            print('Sampai jumpa')
            exit()
    else:
        print("Masukan salah atau akses dilarang! Silahkan coba lagi!")
        command = input(">> ")