#Vraag aan de gebruiker zijn naam, voornaam en geboortedatum (formaat: dd-mm-yyyy) op.
#Genereer hiermee een paswoord door:

def genereer_paswoord(voornaam,naam,geboortedatum):
    paswoord = ""
    #spaties verwijderen
    voornaam = voornaam.replace(' ','')
    naam = naam.replace(' ','')
    #3 letters, 2 letters en 2 cijfers
    paswoord = naam[0:3].lower() + voornaam[0:2].upper() + geboortedatum[3:5] + geboortedatum[8:10]
    return paswoord


voornaam = input(f"Geef uw voornaam op: >")
naam= input(f"Geef uw naam op: >")
geboortedatum = input(f"Geef uw geboortedatum op (dd-mm-yyyy): >")
paswoord = genereer_paswoord(voornaam, naam, geboortedatum)
print(f'Jouw paswoord is; {paswoord}"')