import csv
# from bs4 import BeautifulSoup
# from curl_cffi import requests
# import time
# import urllib.parse
import string as str
import os

# url = 'https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-nonfiction/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }

# response = requests.get(url, impersonate='chrome')

# if response.status_code == 200:

#     parse = BeautifulSoup(response.text, 'html.parser')

#     text1 = parse.find_all('h3', attrs={'class' : 'css-5pe77f'})
#     text2 = parse.find_all('p', attrs={'class' : 'css-hjukut'})

#     with open('index.csv', 'a', newline='', encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
#         writer.writerow(['Title', 'Author'])
#         for col1, col2 in zip(text1, text2):
#             writer.writerow([
#                 col1.get_text().strip(), 
#                 col2.get_text().strip().removeprefix('by ')])

#     print("Successfully bypassed protection and scrapped data")
# else :
#     print("Failed lmao")
# lemari_baju = ["baju", "celana", "kaos kaki"]

# while True: 
#     print("\n==ISI LEMARI==")
#     if lemari_baju == [] :
#         print("Lemari nya kosong dek!")

#     for pakaian in lemari_baju :
#         print("-",pakaian)

#     print("\nPilih operasi!")
#     print("1. Ambil Pakaian")
#     print("2. Tambah Pakaian")
#     print("3. Keluar Program")

#     pilih_aksi = input("Pilih aksi (1/2/3) : ").casefold()

#     match pilih_aksi:
#         case "1" :
#             ambil_pakaian = input(f"Ambil pakaian! ").casefold()
#             if ambil_pakaian in lemari_baju :
#                 lemari_baju.remove(ambil_pakaian)
#                 print(f"{ambil_pakaian} berhasil diambil wak!")
#             else : 
#                 print("ga ada di lemari bos!, coba cari lagi")

#         case "2" :
#             tambah_pakaian = input("Tambah pakaian di lemari: ").casefold()
#             lemari_baju.append(tambah_pakaian)
#             print("Pakaian berhasil ditambah!")

#         case "3" :
#             print("Byeebyeee")
#             break

#         case _ :
#             print("Pilihanmu ga valid weh, pilih 1 2 atau 3 kocak")

# lemari = ["baju", "celana", "kaos", "kemeja", "celana pendek"]

# while True :
#     if lemari == [] :
#         print("Lemari kosong!")
#         break

#     for pakaian in lemari : 
#         print(pakaian)

#     pilih_aksi = input("Mau ambil pakaian? (ya/tidak)")

#     if pilih_aksi == "ya":
#         ambil_pakaian = input("ambil pakaian : ").casefold()
#         if ambil_pakaian in lemari:
#             lemari.remove(ambil_pakaian)
#         else : 
#             print(f"Gak ada {ambil_pakaian} di lemari!")
#     else :
#         mau_tambah_pakaian = input("Tambah pakaian? (ya/tidak) ").casefold()
#         if mau_tambah_pakaian == "ya" :
#             tambah_pakaian = input("Tambah pakaian : ").casefold()
#             lemari.append(tambah_pakaian)
#             print(f"Pakaian {tambah_pakaian} berhasil ditambahkan")
#         else :
#             print("Oke ga nambah apa apa ya.....")

# lemari_baju = ["baju", "celana", "kaos kaki"]

# def tampilin_lemari(isi_lemari):
#     if isi_lemari == [] :
#         print("Kosong wakgeng")
#         return False
#     for pakaian in isi_lemari:
#         print("-", pakaian)
#     return True

# def ambil_pakaian(isi_lemari):
#     pakaian_diambil = input(f"Ambil pakaian! ").casefold()
#     if pakaian_diambil in isi_lemari :
#         isi_lemari.remove(pakaian_diambil)
#         print(f"{pakaian_diambil} berhasil diambil wak!")
#     else : 
#         print("ga ada di lemari bos!, coba cari lagi")

# def tambah_pakaian(isi_lemari):
#     tambah_pakaian = input("Tambah pakaian di lemari: ").casefold()
#     isi_lemari.append(tambah_pakaian)
#     print("Pakaian berhasil ditambah!")


# while True: 
#     tampilin_lemari(lemari_baju)
#     pilih_aksi = input("Pilih aksi (ambil/tambah/keluar) : ").casefold()
#     match pilih_aksi:
#         case "ambil" :
#             ambil_pakaian(lemari_baju)
#         case "tambah" :
#             tambah_pakaian(lemari_baju)
#         case "keluar" :
#             print("Byeebyeee")
#             break
#         case _ :
#             print("Pilihanmu ga valid weh, pilih ambil/tambah/keluar kocak")

csv_file = "rak_buku.csv"

def load_buku():
    buku_sementara = []
    if os.path.exists(csv_file):
        with open (csv_file, mode='r') as file:
            reader = csv.reader(file)
            for baris in reader:
                buku_sementara.append(baris[0])
    return buku_sementara

def save_buku(isi_rak):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for buku in isi_rak:
            writer.writerow([buku])

def lihat_buku(isi_rak):
    if isi_rak == []:
        print("Gak ada buku!")
    else:
        for buku in isi_rak:
            print("-", buku)

def ambil_buku(isi_rak):
    buku_diambil = input("Ambil bukumu : ").casefold()
    if buku_diambil in isi_rak :
        isi_rak.remove(buku_diambil)
        print(f"{buku_diambil} telah diambil!")
    else:
        print("Gak ada bukunya~")

def tambah_buku(isi_rak):
    buku_ditambah = input("Tambah bukumu : ").casefold()
    isi_rak.append(buku_ditambah)
    print(f"{buku_ditambah} berhasil ditambah ke rak buku!")


while True :
    rak_buku = load_buku()

    lihat_buku(rak_buku)

    pilih_aksi = input("Pilih aksi yang mau kamu lakukan! (ambil/tambah/keluar): ").casefold()
    match pilih_aksi:
        case "ambil" :
            ambil_buku(rak_buku)
            save_buku(rak_buku)
        case "tambah":
            tambah_buku(rak_buku)
            save_buku(rak_buku)
        case "keluar":
            print("Terima kasih sudah menggunakan CLI Program ini!")
            break
        case _ :
            print("Pilih dari aksi diatas!")