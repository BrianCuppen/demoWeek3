#Print alle evengetallen tussen 4 en 100 onderelkaar af. 
# #Gebruik een for-lus.

minimum = 4
maximum = 100

for getal in range(minimum, maximum+ 1):
    if getal % 2 == 0:
        print(f"{getal}")


