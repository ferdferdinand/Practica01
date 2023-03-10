import math

eqc = input("Ingresa una ecuación de segundo grado: ")

#Quitamos espacios para evitar problemas con índices
eqc = eqc.replace(" ","")

igual = eqc.find("=")

#Estandarizamos la ecuación y le quitamos lo que no nos sirve
if eqc[igual:] == "=0":
    eqc = eqc[:igual]
else:
    if eqc[igual:][1:2] == "-":
        eqc = eqc[:igual] + "+" + eqc[igual:][2:]
    else:
        eqc = eqc[:igual] + "-" + eqc[igual:][1:]
        
#Separar a de b y c --------------------------------------

#Obtenermos la parte donde se encuentra a, y tomamos el valor como entero
parte_a = eqc[:eqc.find("x")]
eqc = eqc[eqc.find("x")+3:]

if parte_a == "":
    a = 1
elif parte_a == "-":
    a = -1
else:
    a = int(parte_a)
    
#Separar b de c -------------------------------------
x = eqc.find("x")
#Tomamos la parte de b si existe y convertimos el valor a entero
if x != -1:
    parte_b = eqc[:x]
    parte_c = eqc[x+1:]
    
    if parte_b == "+":
        b = 1
    elif parte_b == "-":
        b = -1
    else:
        b = int(parte_b)
    #Tomamos c
    if parte_c == "":
        c = 0
    else:
        c = int(parte_c)
else:
    #Si la parte lineal no existe
    b = 0
    c = int(eqc)

#Imprimimos los coeficientes
print(f"a = {a}, b = {b}, c = {c}")

#Calculamos raices
d = b**2 - 4*a*c

if  d >= 0:
    x1 = (b+math.sqrt(d))/(2*a)
    x2 = (b-math.sqrt(d))/(2*a)
    print("\n\nLas raices son:")
    print("x1 = {x1:.4f}, x2 = {x2:.4f}".format(x1 = x1,x2= x2))
else:
    print("\n\nNo hay solución real")







