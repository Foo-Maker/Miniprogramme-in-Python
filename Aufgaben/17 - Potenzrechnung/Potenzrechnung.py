#!/bin/python3

def input_value(bar):
    foo = input(bar)
    foo = check_num(foo, bar)
    return foo

def check_num(foo, bar):
    try:
        float(foo)
        return foo 
    except:
        error_msg()
        foo = input_value(bar)
        return foo

def error_msg():
    print(f"Die Eingabe war ungültig! ")

def check_ganzzahl(foo, bar):
    try:
        int(foo)
        return foo 
    except:
        error_msg()
        foo = input_value(bar)
        return foo

def abfagen():
    global a
    global b
    foo = "Bitte gieb einen Wert an. : "
    a = input_value(foo)
    foo = "Jetzt einen Wert für den Faktor als Ganzzahl. : "
    b = input_value(foo)
    b = check_ganzzahl(b, foo)
    return a, b

def auswertung(a, b):
    float(a)
    float(b)
    foo = float(a)
    for i in range(1, int(b)):
        foo = foo * float(a)
    print(foo)
    



def main():
    foo = abfagen()
    foo = auswertung(foo[0], foo[1])

main()