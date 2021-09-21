#!/bin/python3

def input_value(bar):
    foo = input(bar)
    foo = check_num(foo, bar)
    return foo

def error_msg(foo):
    print(f"\n Die Eingabe von {foo} ist ungültig. \n Bitte gieb eine gültige Zahl (größer, gleich 2) sein.\n")

def check_num(foo, bar):
    try:
        foo = float(foo)
        if foo >= 2:
            return foo
        else:
            error_msg(foo)
            foo = input_value(bar)
            return foo
    except:
        error_msg(foo)
        foo = input_value(bar)
        return foo

def abfage():
    foo = input_value(f"Bitte geben Sie mir den Wert für die Berechnung der größt möglichen Zweierpotenz.")
    return foo

def berechnung():
    foo = abfage()
    counter = 0
    result = 1
    while result <= foo:
        bar = result
        result = 2 * result
        counter += 1
        if result > foo:
            return bar, counter - 1, foo
        
def main():
    ergebniss = berechnung()
    print(f"Dei kleinste Zweierpotenz von {ergebniss[2]} ist {ergebniss[1]} und beträgt {ergebniss[0]}.")

main()
