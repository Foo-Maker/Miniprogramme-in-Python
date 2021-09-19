def i(wert):
    while True:
        x = float(input(f"{wert}? "))
        if x <= 0:
            print(f"Bitte keine negative Zahl angegeben! Das versuchen wir noch mal.")
        else:
            return(x)

laenge = i("Länge")
breite = i("Breite")
hoehe = i("Höhe")
volumen = laenge * breite * hoehe
oberflaeche = 2 * (laenge * breite) + 2 * ( breite * hoehe) + 2 * (hoehe * laenge)
diagonal = ((laenge * laenge) + (breite * breite) + (hoehe * hoehe))**(0.5) 
print(f"Volume = {volumen} \nOberflaeche ={oberflaeche} \nDiagonal = {diagonal}")