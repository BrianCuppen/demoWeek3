#oefening09, gokken
#we raden een getal tussen 1 en 20
import random

#we laten onze appliccatie een getal kiezen
te_raden_getal = random.randint(1,20)
print(te_raden_getal)
succes = False
aantal_pogingen = 0
#we gaan op zoek naar het getal
while succes == False :
    aantal_pogingen +=1
    gokje = int(input(f"Doe een gokje tussen 1 en 20: >"))
    if gokje == te_raden_getal:
        print(f"Proviciat !")
        print(f"Je hebt {aantal_pogingen} pogingen nodig gehad.")
        succes = True           #<-- noodzakelijk
    elif gokje > te_raden_getal:
        print(f"Het gezochte getal is groter. Prober opnieuw!")
    else:
        print(f"Het gezochte getal is groter. Probeer opnieuw!")




