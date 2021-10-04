from datetime import datetime

#Wat is hier niet goed?

naam = input("Wat is je voornaam?:> ")

def toon_boodschap(uur):
    if uur >= 7 and uur < 12:
        resultaat = f"Goede morgen, {naam}"
    elif uur >= 12 and uur < 13:
        resultaat = f"Joepie het is middag, {naam}"
    elif uur >= 13 and uur < 17:
        resultaat = f"{naam}, goede namiddag"
    elif uur >= 17 and uur < 21:
        resultaat = f"{naam}, goede avond"
    else:
        resultaat = f"Slaapwel, {naam}"
    return resultaat

vandaag = datetime.now()
uur = vandaag.hour
verwelkoming = toon_boodschap(uur)
print(verwelkoming)



# CORRECTIE

# from datetime import datetime

# def geef_boodschap(uur, naam):
#     if uur >= 7 and uur < 12:
#         resultaat = f"Goede morgen, {naam}"
#     elif uur >= 12 and uur < 13:
#         resultaat = f"Joepie het is middag, {naam}"
#     elif uur >= 13 and uur < 17:
#         resultaat = f"{naam}, goede namiddag"
#     elif uur >= 17 and uur < 21:
#         resultaat = f"{naam}, goede avond"
#     else:
#         resultaat = f"Slaapwel, {naam}"

#     return resultaat


# # thuis 4
# vandaag = datetime.now()
# uur = vandaag.hour
# voornaam = input("Wat is je voornaam?:> ")
# verwelkoming = geef_boodschap(uur, voornaam)
# print(verwelkoming)