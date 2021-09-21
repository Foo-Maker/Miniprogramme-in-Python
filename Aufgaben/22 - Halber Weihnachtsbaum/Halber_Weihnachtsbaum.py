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

def halber_baum(foo):
    counter = ""
    for i in range(1, foo + 1):
        counter += "*"
        print(counter)

def main():
    halber_baum(input_value("Wie groß soll der halbe Baum werden? "))
    print("#")

main()