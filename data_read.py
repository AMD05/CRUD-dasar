def read_console():
    print ("==============================================")
    print ("                daftar pekerja                ")
    print ("==============================================")
    data = zip(list_pekerja, list_id, list_hari)
    print ("{:<5} {:<15} {:<15} {:<10}".format('No.', 'Nama', 'ID', 'Hari'))
    print ("==============================================")
    for index, x in enumerate(data):
        nama, nomor, hari = x
        print ("{:<5} {:<15} {:<15} {:<10}".format(index + 1, nama, nomor, hari))

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
    
    if menu == 2 :
        read_console()

    elif menu == 0 :
        break

    else :
        print("opsi tidak ditemukan")
