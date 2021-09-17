count = 0
durchgänge = 4
werte = [] 

def in_wert():
    x = input(f"Bitte geben Sie einen Wert ein. ")
    x = mk_float(x)
    return x

def mk_float(x):
    try:
        x = float(x)
        print(f"Perfect. das war Wert Nummer {count + 1}. \n")
        return x
    except:
        print(f"Das war kein gültiger Wert. \nDas versuchen wir noch einmal.")
        x = in_wert()
        return x
        
while count < durchgänge:
    foo = in_wert()
    werte.append(foo)
    count += 1
    print(f"Wert {count}")

werte.sort()

print(f"der klienste Wert ist {werte[0]}.")
print(f"Der größte Wert ist {werte[-1]}")
print(f"Die Differenz ist ist {werte[-1] - werte[0]}")
print(f"Der Mittelwert der Differenz wäre damit {(werte[-1] - werte[0]) / 2}")


    