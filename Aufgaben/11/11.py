def input_value(foo, bar):
    x = input(f"Bitte gib dein {foo} in {bar} ein. :")
    return (x, foo, bar)

def check_num(foo, a, b):
    try:
        c = float(foo)
        return c
    except:
        print(f"Die Eingabe war ungültig! ")
        d = input_value(a, b)
        d = check_num(d[0], d[1], d[2])
        return d

def eingabe(foo, bar):
    x = input_value(foo, bar)
    x = check_num(x[0], x[1], x[2])
    return x

def check_geschl(foo, a, b):
    if foo.upper() == "M" or foo.upper() == "W":
        if foo.upper() == "M":
            return "Mänlich"
        elif foo.upper() == "W":
            return "Weiblich"
        else:
            print(f"Hier läuft was falsch")
        return foo
    else:
        print(f"Die Eingabe {foo} war ungültig")
        c = input_value(a, b)
        c = check_geschl(c[0], c[1], c[2])
        return c

def eingabe_geschl(foo, bar):
    x = input_value(foo, bar)
    x = check_geschl(x[0], x[1], x[2])
    return x

def calculate_bmi(gewicht, groesse):
    float(gewicht)
    float(groesse)
    return (gewicht / (groesse * groesse))

def bmi_anpassen(foo, alt):
    if alt < 19:
        return "Zu jung für eine diagnose"
    elif alt >= 19 <= 24:
        return foo
    elif alt >= 25 <=34:
        return foo - 1
    elif alt >= 35 <= 44:
        return foo - 2
    elif alt >= 45 <= 54:
        return foo - 3
    elif alt >= 55 <= 64:
        return foo - 4
    elif alt >= 66:
        return foo - 5
    else:
        print(f"Hier liegt ein Fehler vor")
    
def bmi_result(gesch, gew, groe, alt):
    foo = calculate_bmi(gew, groe)
    if gesch == "Mänlich":
        value = bmi_anpassen(foo, alt)
        return value
    elif gesch == "Weiblich":
        value = bmi_anpassen(foo -1, alt)
        return value
    else:
        print(f"Hier liegt ein Fehler vor.")

def catigor(bmi):
    print(f"bmi is {bmi}")
    float(bmi)
    if bmi < 16:
        return "starkes Untergewicht"
    elif bmi >= 16 and bmi <= 16.99:
        return "mäßiges Untergewicht"
    elif bmi >= 17 and bmi <= 18.49:
        return "leichtes Untergewicht"
    elif bmi >= 18.5 and bmi <= 24.99:
        return "Normalgewicht"
    elif bmi >= 25 and bmi <= 29.99:
        return "Übergewicht"
    elif bmi >= 30 and bmi <= 34.99:
        return "Adipositas Grad I"
    elif bmi >= 35 and bmi <= 39.99:
        return "Adipositas Grad II"
    elif bmi >= 40:
        return "Adipositas Grad III"
    else:
       return bmi

groesse = eingabe("Größe", "Meter")
gewicht = eingabe("Gewicht", "Killogram")
alter = eingabe("Alter", "Jahren")
geschlecht = eingabe_geschl("Geschlecht", "( M, oder W )")
bmi = bmi_result(geschlecht, gewicht, groesse, alter)
bmi = round(bmi, 2)
print(f"Dein BMI beträgt {bmi} und damit hast du {catigor(bmi)}")