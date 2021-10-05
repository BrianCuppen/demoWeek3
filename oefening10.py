
totaal_kostprijs_groenten = 0
totaal_kostprijs_fruit = 0
totaal_kostprijs_drank = 0
aantal_producten_groenten = 0
aantal_producten_fruit = 0
aantal_producten_drank = 0

def geef_ticket_per_categorie(categorienaam, totaal, aantal_producten):
    resultaat = ""
    if aantal_producten !=0 :
        resultaat += f"{aantal_producten} Producten zitten in categorie {categorienaam}\n"
        resultaat += f"Totale kostprijs: {totaal} euro\n"
        resultaat += f"Gemiddelde prijs per product: {totaal / aantal_producten:.2f}\n"
    else:
         resultaat = f"Geen producten in de categorie {categorienaam} gevonden."
    return resultaat


aantal_producten = int(input(f"Geef het anatal producten op dat u wilt invoeren:"))
for index in range(0, aantal_producten):
    categorie = input(f"Geef de categorienaam op, [G]roente, [F]ruit of [D]rank:>")
    kostprijs = float(input(f"Geef de kostprijs van het product op: >"))
    if categorie == "G":
        totaal_kostprijs_groenten += kostprijs
        aantal_producten_groenten += 1
    elif categorie == "F":
        totaal_kostprijs_fruit += kostprijs
        aantal_producten_fruit +=1
    elif categorie == "D":
        totaal_kostprijs_drank += kostprijs
        aantal_producten_drank +=1
    else:
        print(f"Foutmelding: Categorie niet herkent!")

print(geef_ticket_per_categorie("groenten", totaal_kostprijs_groenten, aantal_producten_groenten))
print(geef_ticket_per_categorie("fruit", totaal_kostprijs_groenten, aantal_producten_fruit))
print(geef_ticket_per_categorie("drank", totaal_kostprijs_groenten, aantal_producten_drank))

