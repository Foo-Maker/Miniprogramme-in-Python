#!/bin/python3

text_datei = open("text.txt", "r")
text_zeilen = []
woerter = []
woerter_liste = []
sonderzeichen = [",", ".", "?", "*", "#", "+", "=", "", "-", ":", "/", "(", ")", "'", '"', "\\", ";", "@", "_"]
count = 0
count2 = 0

for i in text_datei:
    i.strip(".")
    text_zeilen.append(i)
    count = count + 1
    woerter.extend(i.split())

text_datei.close()

for i in woerter:
    woerter[count2] = woerter[count2].strip(".,:=\/0123456789-")
    for i in sonderzeichen:
        woerter[count2] = woerter[count2].replace(i, "")
    if woerter[count2] not in woerter_liste:
        woerter_liste.insert(-1,woerter[count2])
    count2 = count2 + 1   

woerter_liste.sort()
print(woerter_liste, len(woerter_liste))

ergebniss = open("Ergebniss.txt", "w")
for i in woerter_liste:
    ergebniss.write(f"{i} ")
ergebniss.close()