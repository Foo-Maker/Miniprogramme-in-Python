#!/bin/python3

def input_val(bar):
    foo = input(bar)
    foo = check_num(foo, bar)
    return foo

def error_msg(foo, bar):
    print(f" >> {foo} << ist keine Gültige Eingabe.")
    print(f" Bitte geben Sie mir einen positiven nummerischey Wert an.")
    foo = input_val(bar)
    return foo

def check_num(foo, bar):
    try:
        foo = float(foo)
        if foo > 0 or foo > None:
            return foo
        else:
            error_msg(foo, bar)
            return foo
    except:
        error_msg(foo, bar)
        return foo

def abfagen():
    global gefahren_km
    global preis_liter
    global verbrauch_liter
    gefahren_km = input_val("Bitte tragen Sie hier ein wieviele Kilometer Sie gefahren sind.")
    preis_liter = input_val("Was kostet der Liter Kraftstoff? ")
    verbrauch_liter = input_val("Wieviele Liter wurden verbraucht? ")

def auswertung():
    foo = verbrauch_liter / gefahren_km
    print("Der Verbrauch auf 100 Kilometer beträgt {:.2f}.".format(foo * 100))
    print("Damit kosten 100 Kilometer {:.2f} Euro.".format(foo * 100 * preis_liter))
    print("Die gefahre Strecke koste {:.2f} Euro.".format(verbrauch_liter * preis_liter))

def main():
    abfagen()
    auswertung()

main()