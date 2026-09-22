import math
import json

#opens the json file
with open("D:/PROGRAMMING/practice/conversion_rate.json") as conv_rate:
    rate = json.load(conv_rate)
# print(type(int(rate["conversion_rate"]["eur_idr"])))

#takes input from user
def user_input():
    origin = input("What currency do you want to convert? ")
    target = input("Into : ")
    amount = int(input("Amount : "))
    return (origin, target, amount)
    
#defining the conversion rate 
def conv_rates(origin, target):
    origin;
    target;
    ck = origin + "_" + target 
    rate;
    return rate.get(ck)

#calculating the conversion
def conversion(rate, amount):
    calculation = rate*amount
    return calculation

#validating user_input
origin, target, amount = user_input()

#calling conversion rate
rate = conv_rates(origin, target)

#calling the conversion calculation
result = conversion(rate, amount)

if origin not in ["usd", "idr"]:
    print("Choose the correct currency (usd or idr) : ")
    user_input()
else:
    pass

if target not in ["usd", "idr"]:
    print("Choose the correct target currency (usd or idr) : ")
    user_input()
else:
    pass
    

#showing converted value from result
print("Converted value: ",result)


