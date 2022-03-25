#Liliana Solórzanno Pérez   12 de Agosto 2021 Materia: Pensamiento computacional
"""El siguiente programa nos ayudará a saber el precio final de una compra en videojuegos. Los juegos nuevos cuestan 1000 y los usados 350"""
print("La tienda Gamestore desarrolló este programa para ayudarte a obtener el precio final de tus compras de una forma más eficiente")
print("Si desea comprar videojuegos usados escriba 1 en caso de querer videojuegos nuevos escriba 2")
videojuegos=int(input())

if videojuegos==1:
    print("tenemos los siguientes videojuegos: Mario Kart, Zelda, Call of Duty y Mario Party")
    print("¿Cuántos videojuegos usados deseas comprar?")
    usados=int(input())
    totalu=usados * 350
    print("Tu total a pagar por los juegos usados es de...")
    print(int(totalu))
    print("Si desea seguir comprando seleccione 3 en caso de que no lo desee seleccione 4")
    opción=int(input())
    if opción==4:
        print("fin del programa")
    elif opción==3:
            print("tenemos los siguientes videojuegos nuevos: Warzone, Fornite, Fall Guys, Among Us y Outlast")
            print("¿Cuántos videojuegos nuevos deseas comprar?")
            nuevos=int(input())
            totalun=(nuevos*1000)+totalu
            print("Tu total a pagar es de...")
            print(int(totalun))
             
else:
    print("tenemos los siguientes videojuegos nuevos: Warzone, Fornite, Fall Guys, Among Us y Outlast")
    print("¿Cuántos videojuegos nuevos deseas comprar?")
    nuevos=int(input())
    totaln=nuevos*1000
    print("Tu total a pagar es de...")
    print(int(totaln))

    
    
    
            