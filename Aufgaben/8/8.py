betrag = input("Bitte gieb den Betrag ein: ")
rabat = float(input("Rabat in Prozent: "))
while rabat > 100:
    print(f"Der Rabat beträgt mehr als 100%. Das geht nicht!")
    rabat = float(input("Rabat in Prozent: "))
print(float(betrag) - (float(betrag) * float(rabat) / 100))