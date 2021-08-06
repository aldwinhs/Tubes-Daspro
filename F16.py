# KAMUS
# adminORuser : string

def help(adminORuser): # F16 - Help
    if adminORuser == "admin":
        print('''
        ---HELP---
        register - untuk melakukan registrasi user baru
        login - untuk melakukan login ke dalam sistem
        tambahitem - untuk melakukan penambahan item
        hapusitem - untuk menghapus item
        carirarity - untuk melakukan pencarian berdasarkan rarity
        caritahun - untuk melakukan pencarian berdasarkan tahun ditemukan
        ubahjumlah - untuk mengubah jumlah gadget
        riwayatpinjam - untuk melihat riwayat peminjaman gadget
        riwayatkembali - untuk melihat riwayat pengembalian gadget
        riwayatambil - untuk melihat riwayat pengambilan consumable
        save - untuk menyimpan data
        help - untuk memberikan panduan penggunaan sistem
        exit - untuk keluar dari aplikasi
        ''')
    else:
        print('''
        ---HELP---
        login - untuk melakukan login ke dalam sistem
        carirarity - untuk melakukan pencarian berdasarkan rarity
        caritahun - untuk melakukan pencarian berdasarkan tahun ditemukan
        pinjam - untuk melakukan peminjaman gadget
        kembalikan - untuk mengembalikan gadget
        minta - untuk meminta consumable
        save - untuk menyimpan data
        help - untuk memberikan panduan penggunaan sistem
        exit - untuk keluar dari aplikasi
        ''')