

import random
import string

def genereer_paswoord(minlengte, maxlengte):
    paswoord = ""
    #stap 1, kies een lengte
    lengte = random.randint(minlengte,maxlengte)
    
    for index in range(0, lengte): 
        #stap 2, kies nu elke letter
        #een letter kiezen
        letter = random.choice(string.ascii_letters)
        paswoord += letter

    return paswoord


min_lengte = int(input(f"Geef de minimum lengte op: >"))
max_lengte = int(input(f"Geef de maximum lengte op: >"))
paswoord = genereer_paswoord(min_lengte,max_lengte)
print(f"{genereer_paswoord(min_lengte, max_lengte)}")