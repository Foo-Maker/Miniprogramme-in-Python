#!/bin/python3

def input_value(bar):
    foo = input(bar)
    foo = check_num(foo, bar)
    return foo
    
def check_num(foo, bar):
    try:
        int(foo)
        if int(foo) > 0:
            return foo
        else:
            error_msg(foo)
            foo = input_value(bar)
            return foo
    except:
        error_msg(foo)
        foo = input_value(bar)
        return foo

def error_msg(foo):
    print(f"Die Eingabe von {foo} ist ungültig. \nEs werden nur positive Ganzzahlen erlaubt.")

def berechnung(bar):
    foo = input_value(bar)
    int(foo)
    bar = 1
    count = 1
    for i in range(1, int(foo) + 1):
        bar = bar * count
        count = count + 1
    return bar, foo

def main():
    foo = berechnung(f"Bitte geben Sie mir einen Wert für die Berechnung einer Fakultät. : ")
    print(f"Die Fakultät von {foo[1]} ist {foo[0]}. ")

main()