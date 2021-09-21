#!/bin/python3

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

def stars(foo):
    bar = ""
    for i in range(1, foo + 1):
        bar += "*"
    print(bar)

def rows(foo):
    for i in range(1, foo + 1):
        stars(10)

def main():
    rows(input_value("Bitte geben Sie eine Zahl ein: "))

main()