#!/bin/python3

"""
    Dies ist einfach eine modifizierte Version von der Aufgabe 20
"""

def input_value(bar):
    foo = input(bar)
    foo = check_num(foo, bar)
    return foo

def check_num(foo, bar):
    try:
        foo = int(foo)
        if int(foo) > 0:
            return foo
        else:
            error_msg(foo)
            foo = input(bar)
            return foo
    except:
        error_msg(foo)
        foo = input(bar)
        return foo

def error_msg(foo):
    print(f"Die Eingabe von {foo} ist ungültig. Bitte geben Sie eine positive Ganzzahlen an.")

def rows(bar, foo):
    for i in range(1, foo + 1):
        star = ""
        for x in range(1, bar + 1):
            star += "*"
        print(star)

def main():
    rows(input_value("Wieviele Sterne sollen in eine Zeile? "), input_value("Wieviele Zeilen soll ich ausgeben? "))

main()