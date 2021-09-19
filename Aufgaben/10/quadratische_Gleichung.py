def input_value():
    foo = input(f"Bitte gieb mir eine Zahl. ")
    foo = check_num(foo)
    return foo

def check_num(x):
    try:
        foo = float(x)
        return foo
    except:
        print(f"{x} ist nicht gültig.")
        foo = input_value()
        foo = check_num(foo)
        return foo

def berechnung():
    a = input_value()
    b = input_value()
    c = input_value()
    foo = ((b * b) - (4 * a * c))
    return foo

def auswertung():
    foo = berechnung()
    if foo < 0:
        return ("keine Lösung", foo)
    elif foo == 0:
        return ("eine Lösung", foo)
    elif foo > 0:
        return ("zwei Lösungen", foo)
    else:
        print(f"In der Auswertung gieb es einen Fehler.")
        return foo

foo = auswertung()
print(f"Für das Ergebniss von {foo[1]} gieb es {foo[0]}.")