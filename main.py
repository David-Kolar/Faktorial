from sympy.ntheory import factorint

def out(n):
    with open("output", "w") as file:
        file.write(n)

def inp():
    with open("input") as file:
        for line in file:
            cislo, soustava = line.split()
    return int(cislo), int(soustava)

def main():
    cislo, soustava = inp()
    faktorizace = factorint(soustava)
    delitel = list(faktorizace.items())[-1][0]
    cetnost = list(faktorizace.items())[-1][1]
    v = 0
    while(cislo > 1):
        cislo //= delitel
        v += cislo
    v //= cetnost
    out(str(v))

main()

