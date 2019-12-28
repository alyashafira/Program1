from view.view_nilai import nyari,cetak,header,notoption
from view.input_nilai import input_data,ubah,hapus
header()
while True:

    c = input("\nPilih Opsi: ")

    # KELUA PROGRAM
    if c.lower() == 'k':
        print("++++++++ PROGRAM TELAH SELESAI DIJALANKAN ++++++++")
        ext = input("\nTekan ENTER Untuk Keluar")
        if ext == '':
            break
        else:
            break

    # TAMPILKAN LIST DATA
    elif c.lower() == 'l':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == 't':
        input_data()

    # EDIT DATA
    elif c.lower() == 'u':
        ubah()

    # MENCARI DATA
    elif c.lower() == 'c':
        nyari()

    # HAPUS DATA
    elif c.lower() == 'h':
        hapus()

    else:
        notoption()
