#Programa Sistema Acuario Aqua
#Tarea 3
from datetime import datetime

def calculo_total(dulce,salada):  
    
    return(dulce*200 + salada*500)
    
      
print(" * * * * * Bienvenido al Sistema Acuario Aqua  * * * * \n")
now = datetime.now()
print(" Hoy estamos a", now )
print("")
print(" - - - Tenemos estos tipos de peces - - -")
print("\t Agua dulce $200 c/u")
print("\t Agua salada $500 c/u")
print("")

p_dulce = int(input("¿Cuántos peces de agua dulce deseas comprar? "))
p_salada = int(input("¿Cuántos peces de agua salada deseas comprar? "))

print("Tu total a pagar es:",calculo_total(p_dulce,p_salada))
print("")

if calculo_total(p_dulce,p_salada)>1500:
        print("Felicidades! Ganaste un premio, ¿Cuál quieres? ")        
        print("\t Opción 1: Un pez extra de agua dulce")
        print("\t Opción 2: Alimento vivo")
        print("\t Opción 3: Limpieza de la pecera gratis!")
        print("")
        opcion = int(input("Elige una opción [1] [2] [3]: "))
        
        if opcion == 1:
            print("Elegiste - Un pez extra de agua dulce! ")
        elif opcion == 2:
            print("Elegiste - Alimento vivo! ")
        elif opcion == 3:
            print("Elegiste - Limpieza de la pecera gratis!")
        else:
            print("Opción no válida! Lo siento")



