#Print de som van de eerste 100 getallen. Gebruik een for-lus.

som = 0

for getal in range(1, 101): #getallen van 1 tot 100.
    #som = 0 + 1 = 1
    #som = 1 + 2 = 3
    #som = 3 + 3 = 6
    #som = som  + ... = ...
    som = som + getal

print(f"De som vand e eerste 100 getallen is: {som}")