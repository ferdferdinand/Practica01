
#Se ingresa la antigüedad del trabjador
ant = int(input("Ingrese los años de antigüedad: "))
#Se ingresa el género del trabajador
genero = input("Ingresa 'f' o 'm', según sea el caso: ").lower()
print()
#Cantidad de productos vendidos
c1 = int(input("Ingresa la cantidad de artículos vendidos del producto 1 durante el mes: "))
c2 = int(input("Ingresa la cantidad de artículos vendidos del producto 2 durante el mes: "))
c3 = int(input("Ingresa la cantidad de artículos vendidos del producto 3 durante el mes: "))
c4 = int(input("Ingresa la cantidad de artículos vendidos del producto 4 durante el mes: "))


#Precio por producto
P1 = 2040
P2 = 5567.50
P3 = 850.38
P4= 1000

#Comisiones del trabajador por años de antigüedad
if ant < 1:
    #El monto de comisión sería la suma de la comisión de cada producto que vendió
    monto = c1*P1*0.13 + c2*P2*0.02 + c3*P3*0.185 + c4*P4*0.04
elif 1 <= ant < 3:
    monto = c1*P1*0.15 + c2*P2*0.05 + c3*P3*0.20+ c4*P4*0.06
elif 3 <= ant < 5:
    monto = c1*P1*0.155 + c2*P2*0.07 + c3*P3*0.22 + c4*P4*0.077
else:
    monto = c1*P1*0.18 + c2*P2*0.10 + c3*P3*0.25 + c4*P4*0.122
    #Si es femenino, el monto aumenta 2%
    if genero == "f":
        monto *= 1.02

#Imprimimos su comisión mensual
print("\n\nEl monto que recibirá de comisiones este mes es de: ${monto:.2f}".format(monto = monto))        
