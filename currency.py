import math

while True:
    origin = input("What currency do you want to convert? ")
    target = input("Into : ")
    amount = int(input("Amount : "))

    usd_idr = amount*16000
    idr_usd = amount/16000

    if origin == "usd" :
        if target == "idr":             
            print("Converted value: ", usd_idr, "Rupiah")

    if origin == "idr" :
        if target == "usd":
            print("Converted value: ", idr_usd, "Dollar")

