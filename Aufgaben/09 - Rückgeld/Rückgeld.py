betrag = float(input("Bitte gieb den Betrag ein: "))
gezahlt = float(input("Wieviel wurde gezahlt? "))

if gezahlt < betrag:
    print("Da fehlt noch was!")
elif gezahlt == betrag:
    print("Punktlandun! Es wurde passend gezahlt")
elif gezahlt >= betrag:
    print(f"Du bekommst {gezahlt - betrag} wieder.")
else:
    print("Hier liegt ein Fehler vol.")