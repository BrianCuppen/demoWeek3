#Print de som van de eerste 100 getallen. 
#Gebruik hiervoor een while-lus.

def bereken_som_getallen_while(aantal):
    som = 0
    index = 0 #<--Hiermee houden we bij waar we zitten

    while index <= 100:
        som = som + index     #<--som += index (verkorte notatie)
        index += 1     #vergeet de index niet te verhogen anders oneindige lus !
    return som


print(f"Sum of 1 till 100: {bereken_som_getallen_while(100)}.")