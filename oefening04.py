#Print alle onevengetallen tussen 10 en 129 naastelkaar af. 
#Gebruik een for-lus.

minimum = 10
maximum = 129
getal_string = ""

for getal in range(minimum, maximum+ 1):
    if getal % 2 == 1:
        #getal_string = "" + 10 = "10"
        getal_string = getal_string + str(getal) + ","
       
print(f"{getal_string}")
