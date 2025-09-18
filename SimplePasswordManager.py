import json
import os

file_name = "password.json"

def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def add_account():
    print("== Tambah Akun Baru ==")
    nama_akun = input("Akun: ").capitalize()
    username = input("Username: ")
    password = input("Password: ")
    data = load_data()
    data.append({"Akun": nama_akun, "Username": username, "Password": password})
    save_data(data)
    print("Akun Berhasil Ditambahkan!!\t\n")
    pass

def see_account():
    print("== Daftar Akun ==")
    data = load_data()
    if data:
        for i, akun in enumerate(data):
            print(f"{i+1}. Akun: {akun['Akun']} - Username: {akun['Username']} - Password: {akun['Password']}")
            pass
        print("")
    else:
        print("Tidak Ada Akun!!")
        print("")

        
def delete_account():
    print("=== Hapus Akun ===")
    data = load_data()
    if data:
        for i, akun in enumerate(data):
            print(f"{i+1}. Akun: {akun['Akun']} - Username: {akun['Username']} - Password: {akun['Password']}")
            pass
        print("")
        try:
            del_account = int(input("Hapus Akun: "))
            if del_account >= 1 and del_account <= len(data):
                data.remove(data[del_account-1])
                print("Akun Berhasil Dihapus!!")
                print("")
            else:
                print("Akun Tidak Ditemukan!!")
                print("")
            save_data(data)
        except ValueError:
            print("Masukkan Angka!!")
    else:
        print("Tidak Ada Akun!!")
        print("")

def menu():
    print("=== Password Manager ===")
    print("1. Tambah Akun")
    print("2. Lihat Semua Akun")
    print("3. Hapus Akun")
    print("4. Keluar")
    print("")
    

while True:
    menu()
    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("Masukkan angka yang benar!\n")
        continue

    if pilihan == 1:
        add_account()
    elif pilihan == 2:
        see_account()
    elif pilihan == 3:
        delete_account()
    elif pilihan == 4:
        print("Terima kasih sudah menggunakan Password Manager!")
        break
    else:
        print("Menu tidak tersedia!\n")