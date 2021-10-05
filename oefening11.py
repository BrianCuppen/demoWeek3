#Vraag aan de gebruiker twee jaartallen op. 
#Print de schrikkeljaren tussen deze twee jaartallen af.\
#schikkeljaar<> jaartal deelbaar door 4, als het deelbaar is door 100
#uitzondering op de uitzondering, jaren deelbaar door 400 zijn wel schrikkeljaren !
#deze functie controleert of het jaartal een schrikkeljaar is

def is_schikeljaar(jaartal):
    #True --> bij een schrikkeljaar, False in het andere geval
    if (jaartal % 4 == 0) and (jaartal %100 !=0 ) or (jaartal % 400 == 0):
        return True
    return False

jaartal1 = int(input(f"Geef het eerste jaartal op: >"))
jaartal2 = int(input(f"Geef het tweede jaartal op: >"))
#print enkel de schrikkeljaren af ---> overloop alle jaartallen en doe een controle

for index in range(jaartal1, jaartal2 +1):
    if is_schikeljaar(index) == True:
        print(f"{index} is een schrikkeljaar.")
