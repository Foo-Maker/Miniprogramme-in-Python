#!/bin/python3

def input_value(stage):
    bar = ["die länge des Grundstücks in Meter", "die breide des Grundstücks in Meter", "den Quatmeterpreis in Euro", "die Provision in Prozent", "den aktuellen Steuersatz in Prozent"]
    x = input(f"Bitte geben Sie {bar[stage]} ein. : ")
    foo = check_num(x, stage)
    return foo

def wrong_input(stage):
    print(f"Die Eingabe war ungültig. Es wird nur eine Zahl akzeptiert. ")
    bar = input_value(stage)
    a = check_num(bar, stage)
    return a

def check_num(foo, stage):
    try:
        bar = float(foo)
        if bar > 0 or bar > None:
            return bar
        else:
            print(f"Der Wert muss schon größer 0 sein.")
            return wrong_input(stage)
    except:
        bar = wrong_input(stage)
        return bar

def stages(e):
    foo = input_value(e)
    return foo

def berechnung_flaeche():
    return laenge_grundstueck * breite_grundstueck

def grundstueck_preis():
    foo = berechnung_flaeche()
    return quadratmeterpreis * foo 

def mwst():
    foo = grundstueck_preis()
    return foo - (foo / (steuersatz + 100) * 100)

def markler_provision():
    foo = (grundstueck_preis() / 100 * provision)
    return foo

def gesamtpreis():
    foo = markler_provision() + grundstueck_preis()
    return foo

def auswertungen():
    print("Das Grundstücks hat eine Fläche von {:.2f} Quadratmeter.".format(berechnung_flaeche()))
    print("Es wird {:.2f}".format(grundstueck_preis()), " Eure kosten wovon {:.2f} Mehrwertsteuer.".format(mwst()))
    print("Der Markler erhält noch {:.2f} Euro.".format(markler_provision()))
    print("Dadurch haben wir einen Gesantpreis von {:.2f} Euro.".format(gesamtpreis()))

def main():
    global laenge_grundstueck 
    global breite_grundstueck
    global quadratmeterpreis
    global provision
    global steuersatz
    laenge_grundstueck = stages(0)
    breite_grundstueck =  stages(1)
    quadratmeterpreis =  stages(2)
    provision =  stages(3)
    steuersatz =  stages(4)
    auswertungen()

main()