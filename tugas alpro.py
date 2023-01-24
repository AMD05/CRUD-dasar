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

list_pekerja=["agil", "surya", "aldi"]
list_id=[101, 102, 103]
list_hari=["senin", "selasa", "rabu"]

list_menu = ["1. create data pekerja", "2. read data pekerja", "3. update data pekerja", "4. delete data pekerja"]
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
        create_console()

    elif menu == 2 :
        read_console()

    elif menu == 3 :
        update_console()

    elif menu == 4 :
        delete_console()

    else :
        break
