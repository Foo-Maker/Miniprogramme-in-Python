laenge = float(input("Länge? "))
breite = float(input("Breite? "))
hoehe = float(input("Höhe? "))
volumen = laenge * breite * hoehe
oberflaeche = 2 * (laenge * breite) + 2 * ( breite * hoehe) + 2 * (hoehe * laenge)
diagonal = ((laenge * laenge) + (breite * breite) + (hoehe * hoehe))**(0.5) 
print(f"Volume = {volumen} \nOberflaeche ={oberflaeche} \nDiagonal = {diagonal}")