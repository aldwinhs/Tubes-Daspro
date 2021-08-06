import os

def save(dir,datas,header,file): # F15 - Save Data
    # CONVERT SEMUA DATA KEMBALI MENJADI STRING
    def convert_datas_to_string(header, datas):
        string_data = ";".join(header) + "\n"
        for arr_data in datas:
            arr_data_all_string = [str(var) for var in arr_data]
            string_data += ";".join(arr_data_all_string)
            string_data += "\n"
        return string_data

    # DIRECTORY YANG SAAT INI
    pathOpen = "./"+dir+"/"+file

    # PROSES SAVE
    for subdirs in os.walk('.'): 
        for f in subdirs:
            # JIKA DIRECTORY SUDAH ADA, MAKA DATA AKAN OVERWRITE
            if os.path.exists(dir):
                datas_as_string = convert_datas_to_string(header, datas)
                f = open(pathOpen, "w")
                f.write(datas_as_string)
                f.close()
                break
            else:
                # JIKA DIRECTORY BELUM ADA, MAKA AKAN DIBUAT FOLDER BARU DENGAN MK. DIR
                parent_dir = "./"
                pathNew = os.path.join(parent_dir, dir) # DIRECTORY BARU
                os.mkdir(pathNew)

                datas_as_string = convert_datas_to_string(header, datas)
                f = open(pathOpen, "w")
                f.write(datas_as_string)
                f.close()
                break
