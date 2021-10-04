def bereken_som(getal1, getal2):
    som = getal1 + getal2
    return som


# demo debugging: voorspel wat de gebruiker (niet) zal zien...
waarde1 = input("Geef jouw eerste getal op: ")
waarde2 = input("Geef jouw tweede getal op: ")
print(f"De som van beide getallen is {bereken_som(waarde1, waarde2)}.")
