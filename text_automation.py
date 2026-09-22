# file_name = "text.txt"

# text = "Coba lihat ini!"

# with open(file_name, "w") as f :
#     f.write(text)
# print("File created succesfully")

file_name2  = "writer.txt"
text2 = "St. Michael the Archangel, Pray for Us"

with open(file_name2, "w") as f :
    f.write(text2)
print("Succesfully get it done!")

with open(file_name2, "r") as f:
    content = f.read()
    print(content)
