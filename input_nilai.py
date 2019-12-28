def input_data():
    from model.daftar_nilai import tambah_data
    while (True):
        nama = input("Nama Mahasiswa   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM Mahasiswa    : "))
            if nim == '':
                print('Masukan NIM Mahasiswa dengan Angka')
        except ValueError:
            print('Masukan NIM Mahasiswa dengan Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("Nilai Tugas   : "))
            if tugas == '':
                print('Masukan Nilai TUGAS dengan Angka')
        except ValueError:
            print('Masukan Nilai TUGAS dengan Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("Nilai UTS     : "))
            if uts == '':
                print('Masukan Nilai UTS dengan Angka')
        except ValueError:
            print('Masukan Nilai UTS dengan Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("Nilai UAS     : "))
            if uas == '':
                print('Masukan Nilai UAS dengan Angka')
        except ValueError:
            print('Masukan Nilai UAS dengan Angka')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)
    print("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar   ")


def ubah():
    from model.daftar_nilai import ubah_data
    ubah_data(nama=input("Masukan Nama Untuk Perubahan Data : "))


def hapus():
    from model.daftar_nilai import hapus_data
    hapus_data(nama=input("Masukan Nama Yang Ingin Dihapus : "))
    print("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar   ")


def cari():
    from model.daftar_nilai import cari_data
    cari_data(nama=input("Masukan nama yang di cari : "))

