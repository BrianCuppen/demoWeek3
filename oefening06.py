#Vraag aan de gebruiker volgende 2 getallen op:
#-een startwaarde
#-een stopwaarde
# Printeen lijstvanalle getallen tussen de twee opgegeven grenzen (grenzen inclusief) 
#die deelbaar door 7 maar geen veelvoud van 5zijn.

getal1 = int(input(f"Geef een startwaarde op: >"))
getal2 = int(input(f"Geef een tweede getal: >"))
 
if getal1 > getal2:
    getal1 , getal2 = getal2, getal1
for getal in range(getal1, getal2 + 1):
    if getal %7 == 0 and getal %5 != 0:
        print(f"{getal}")