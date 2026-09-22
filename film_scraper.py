# import csv
# from bs4 import BeautifulSoup
# from curl_cffi import requests
# import time
# import urllib.parse
import string as str

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
lemari_baju = ["baju", "celana", "kaos kaki"]

while True: 
    print("\n==ISI LEMARI==")
    if lemari_baju == [] :
        print("Lemari nya kosong dek!")

    for pakaian in lemari_baju :
        print("-",pakaian)

    print("\nPilih operasi!")
    print("1. Ambil Pakaian")
    print("2. Tambah Pakaian")
    print("3. Keluar Program")

    pilih_aksi = input("Pilih aksi (1/2/3) : ")

    match pilih_aksi:
        case "1" :
            ambil_pakaian = input(f"Ambil pakaian! ").casefold()
            if ambil_pakaian in lemari_baju :
                lemari_baju.remove(ambil_pakaian)
                print(f"{ambil_pakaian} berhasil diambil wak!")
            else : 
                print("ga ada di lemari bos!, coba cari lagi")

        case "2" :
            tambah_pakaian = input("Tambah pakaian di lemari: ").casefold()
            lemari_baju.append(tambah_pakaian)
            print("Pakaian berhasil ditambah!")

        case "3" :
            print("Byeebyeee")
            break

        case _ :
            print("Pilihanmu ga valid weh, pilih 1 2 atau 3 kocak")