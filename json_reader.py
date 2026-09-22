import json
import os
import pathlib


# cwd = os.getcwd()
# files = os.listdir(cwd)
# print("Files in %r: %s" & (cwd, files))

with open("D:/PROGRAMMING/practice/conversion_rate.json") as conv_rate:
    file = json.load(conv_rate)

print(file["conversion_rate"]["eur_idr"])

#[] -> list in json
#{} -> dictionaries
#both cannot be accessed the same way as one another