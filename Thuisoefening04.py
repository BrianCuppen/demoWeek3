
def is_schrikkeljaar(startjaar, eindjaar):
    if startjaar > eindjaar:
        print("Ongeldige input")
    else:
        while(startjaar <= eindjaar):
            if startjaar % 100 == 0 and startjaar % 400 == 0:
                print(f"{startjaar} is een schrikkeljaar")
                startjaar += 1
            if startjaar % 4 == 0 and startjaar % 100 != 0:
                print(f"{startjaar} is een schrikkeljaar")
                startjaar += 1
            else:
                startjaar += 1



startjaar = int(input("Geef het startjaar op: >"))
eindjaar = int(input("Geef het eindjaar op: >"))


is_schrikkeljaar(startjaar, eindjaar)
