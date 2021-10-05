#Schrijf een functie ‘swap’ die twee strings binnenkrijgt.
#De functie stelt één nieuwe string op waarbij de twee letters van elk woord worden omgewisseld en beide nieuwe woorden door een spatie gescheiden worden.



def swap (woord1, woord2):
    resultaat = ""
    resultaat = woord2[0:2] + woord1[2:] + " " + woord1[0:2] + woord2[2:]
    return resultaat


woord1 = input(f"Geef het eerste woord op: >")
woord2 = input(f"Geef het tweede woord op: >")
resultaat = swap(woord1, woord2)
print(resultaat)