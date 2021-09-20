#!/bin/python3

from random import randint

def input_value(a, b):
    foo = input(f"Was ist {a} plus {b} ? ")
    return foo

def random_value():
    return randint(0, 100)

def auswertung():
    a = random_value()
    b = random_value()
    foo = input_value(a, b)
    bar = a + b
    x = foo.isdigit()
    if x != False:
        if foo == str(bar):
            print(F"Glückwursch! {a} plus {b} ist {foo}.")
        else:
            print(f"Leider falsch. {a} plus {b} ist {a + b}.")
    elif foo.upper() == "ENDE":
        exit("Auf wiedersehen! Bis zum nächsten mal.")
    else:
        print(f"Ich kann nul mit Zahlen rechnen. ")

def main():
    while True:
        auswertung()

main()