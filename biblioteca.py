def imprime_Nome(nome):
    print(f"Nome:{nome}")


def piramide(n):
    for x in range(1,   n+1):
        for y in range(0,x):
             print(x, end=" ")
        print()



def contaVogais(texto):
    for x in range(len(texto)):
        if texto[x] == "a" or texto[x] == "e" or texto[x]=="i" or texto[x]=="o" or texto[x]=="u":
            cont=cont+1
    print(cont)

