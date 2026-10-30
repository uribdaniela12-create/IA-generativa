#ordenar.py  plantilla inicial
# Paso 1: comparar dos números y mostrarlos de menor a mayor
#a = int(input("Primer número: "))
#b = int(input("Segundo número: "))

#if a <= b:
#    print(a, b)
#else:
  #  print(b, a)

# Paso 2 (con tu TL): pide un tercer número c y muestra los tres de menor a mayor.
# Solo con if, else y comparaciones: sin listas, ciclos ni sorted().
# ordenar.py

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

if a <= b:
    if b <= c:
        print(a, b, c)
    else:
        if a <= c:
            print(a, c, b)
        else:
            print(c, a, b)
else:
    if a <= c:
        print(b, a, c)
    else:
        if b <= c:
            print(b, c, a)
        else:
            print(c, b, a)

