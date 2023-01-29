def read_console():
    print ("==============================================")
    print ("|               daftar pekerja               |")
    print ("==============================================")
    data = zip(list_pekerja, list_id, list_hari)
    print ("| {:<5}| {:<20}| {:<5}| {:<7}|".format('No.', 'Nama', 'ID', 'Hari'))
    print ("==============================================")
    for index, x in enumerate(data):
        nama, nomor, hari = x
        print ("| {:<5}| {:<20}| {:<5}| {:<7}|".format(index + 1, nama, nomor, hari))

def create_console(nama, nomor, hari):
    list_pekerja.append(nama)
    list_id.append(nomor)
    list_hari.append(hari)
    string_nama = ",".join(list_pekerja)
    string_id = ",".join(str(x) for x in list_id)
    string_hari = ",".join(list_hari)
    open_file = open("ListPekerja.txt", "w")
    open_file.write(string_nama + "\n")
    open_file.write(string_id + "\n")
    open_file.write(string_hari)
    open_file.close()

def delete_console(hapus) :
    list_pekerja.pop(hapus - 1)
    list_id.pop(hapus - 1)
    list_hari.pop(hapus - 1)
    string_nama = ",".join(list_pekerja)
    string_id = ",".join(str(x) for x in list_id)
    string_hari = ",".join(list_hari)
    open_file = open("ListPekerja.txt", "w")
    open_file.write(string_nama + "\n")
    open_file.write(string_id + "\n")
    open_file.write(string_hari)
    open_file.close()

def update_console(ubah, nama, nomor, hari) :
    list_pekerja[ubah - 1] = nama
    list_id[ubah - 1] = nomor
    list_hari[ubah - 1] = hari
    string_nama = ",".join(list_pekerja)
    string_id = ",".join(str(x) for x in list_id)
    string_hari = ",".join(list_hari)
    open_file = open("ListPekerja.txt", "w")
    open_file.write(string_nama + "\n")
    open_file.write(string_id + "\n")
    open_file.write(string_hari)
    open_file.close()

open_file = open("ListPekerja.txt", "r")
count = 0

list_pekerja = []
list_id = []
list_hari = []

while True:
    count += 1
    data = open_file.readline()
    
    if not data:
        break
    
    if count == 1 :
        list_pekerja = data.rstrip().split(",")
    
    elif count == 2 :
        list_id = data.rstrip().split(",")

    elif count == 3 :
        list_hari = data.rstrip().split(",")

list_menu = ["1. create data pekerja", "2. read data pekerja", "3. update data pekerja", "4. delete data pekerja", "0. keluar program"]
while True :
    print ("=======================")
    print ("       menu utama      ")
    print ("=======================")
    for y in list_menu: 
        print(y) 
    print ("=======================")
    print (" pilih opsi : ")
    menu =int(input()) 
    if menu == 1 :
        print ("Masukkan Nama : ")
        nama = str(input())
        print ("Masukkan ID : ")
        nomor = int(input()) 
        print ("masukkan Hari : ")
        hari = str(input())
        create_console(nama, nomor, hari)
    elif menu == 2 :
        read_console()

    elif menu == 3 :
        print ("Data yang diubah : ")
        ubah = int(input())
        if ubah <=len(list_pekerja) :
            print ("Masukkan Nama : ")
            nama = str(input())
            print ("Masukkan id pekerja : ")
            nomor = int(input())
            print ("masukkan hari : ")
            hari = str(input())
            update_console(ubah, nama, nomor, hari)
            read_console()

    elif menu == 4 :
        print("Data yang akan di hapus : ")
        hapus = int(input())
        if hapus <=len(list_pekerja):
            delete_console(hapus)
            read_console()

    elif menu == 0 :
        break

    else :
        print("opsi tidak ditemukan")
    print("==============================================")