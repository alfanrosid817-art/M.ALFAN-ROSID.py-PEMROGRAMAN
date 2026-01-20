#NAMA  :M.ALFAN ROSID
#KELAS  :1A PENDIDIKAN INFORMATIKA
#NPM   :250305029

import math


print("====================== APLIKASI BANGUN DATAR =======================")
print("=================== TUGAS UAS PEMROGRAMAN DASAR 2026 ==================== ")

nama = input ("Masukkan Nama Anda: ")
print(f"Halo {nama},Selamat Datang Di aplikasi Bangun Datar!")

while True :
    print("\n Daftar Bangun Datar : ")
    print("1. Persegi")
    print("2. Persegi Panjang ")
    print("3. Lingkaran ")
    print("4. Segitiga ")
    
    pilihan = input ("Pilih Bangun Datar (1-4): ")
    
    if pilihan =="1" :
        sisi = float(input("Masukkan Sisi Persegi: "))
        luas = sisi * sisi
        keliling = 4 * sisi
        
    elif pilihan == "2" :
        panjang = float (input("Masukkan Panjang: "))
        lebar = float (input('Masukkan Lebar: '))
        luas = panjang * lebar
        keliling = 2 * (panjang+lebar)
        
    elif pilihan == "3" :
        r = float (input("Masukkan Jari-Jari: "))
        luas = math.pi * r * r
        keliling = 2 * math.pi*r
    
    elif pilihan == "4" :
        alas = float (input("Masukkan Alas : "))
        tinggi = float (input("Masukkan Tinggi: "))
        sisi =float(input("Masukkan Sisi Miring: "))
        luas =0.5 * alas * tinggi
        keliling = alas + tinggi + sisi
        
    else :
        print("pilihan tidak valid! ")
        continue
    
    print(f"\nluas      ={luas}")
    print(f"keliling    ={keliling}")
    
    ulang = input ("\nHitung lagi (yes/no): ")
    if ulang.lower() != "y" :
        print ("\n Terimakasih Telah Menggunakan Aplikasi Ini. ")
        break
    
print ("        APLIKASI PERHITUNGAN      ")
print ("=======Program Sudah Selesai=======")