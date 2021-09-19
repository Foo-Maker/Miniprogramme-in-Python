#!/bin/python3

kandidaten = {}
result = {}

def open_liste():
    return open("Kandidaten.txt", "r")

def create_dict():
    counter = 0
    kandidaten[counter] = '>> ENDE <<'
    foo = open_liste()
    for i in foo:
        i = i.strip()
        counter = counter + 1
        kandidaten[counter] = i 
        result[i] = 0 
    return kandidaten

def input_value():
    auflistung()
    foo = input(f"\nBitte geben Sie Ihre Wahl ein. : ")
    foo = check_num(foo)
    return foo

def check_num(foo):
    try:
        foo = int(foo)
        if foo == 0:
            run = True
        elif foo > 0 and foo < len(kandidaten):
            return foo
        elif foo >= len(kandidaten):
            print(f"So viele Kandidaten haben wir nicht.")
            foo = input_value()
            return foo
    except:
        print(f"Die Eingabe muss eine Zahl sein.\n")
        foo = input_value()
        return foo

def auflistung():
    counter = 1
    print(f"Zum Beenden bitte 0 eintippen")
    while counter < len(kandidaten):
        print(f"Kandidat Nr. {counter} ist {kandidaten[counter]}.")
        counter = counter + 1
    
def abfagen():
    run = False
    while run != True:
        foo = input_value()
        try:
            if foo == 0 or foo == None:
                run = True
            else:
                bar = kandidaten[foo]
                result[bar] = result[bar] + 1
        except:
            print(f"Hier rennt ein Fehler auf. foo ist {foo}. \nfoo darf aber nur 0, None bzw eine Zahl zwischen 1 und {len(kandidaten)} sein.")
    print(f"Die Auswertung wird gestartet…\n")
    auswertung()

def ranking_result():
    ranking = sorted(result.items(), key=lambda x:x[1], reverse=True)
    ranking = dict(ranking)
    return ranking

def auswertung():
    foo = 1
    bar = ranking_result()
    for i in bar:
        print(f"{i} hat {result[i]} Stimmen erhalten.")
    res = list(bar.keys())[0]
    print(f"Damit hat des Kandidat {res} mit {bar[res]} Stimmen die Wahl gewonnen.")

create_dict()
abfagen()
