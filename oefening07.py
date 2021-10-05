
#Vraag aan de gebruiker volgende 3 getallen op:

#Deze functie geeft een string terug besetaande uit getallen
#Die moeten afgeprint worden
def geef_lijst_getallen(start, stap, aantal):
    resultaat = "De lijst met getallen is:\n"
    stop = start + (stap * aantal)
    for getal in range(start,stop, stap):
        resultaat += str(getal) + ","  #<--- resultaat = resultaat + getal


    return resultaat

startwaarde = int(input(f"Geef de startwaarde op: >"))
stapgroote = int(input(f"Geef een positieve stapgroote op: >"))
aantal_getallen = int(input(f"Geef het aantal getallen op: >"))
tekst = geef_lijst_getallen(startwaarde, stapgroote, aantal_getallen)
print(tekst)

