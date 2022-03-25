#Programa muebleria
def calculo_total(t_s,t_c,c_s):
    descuento = 0
    
    if t_s=='B':
        costo_silla = 700
    elif   t_s=='E':
         costo_silla = 900
    elif   t_s=='L':
        costo_silla = 1500    
    
    total = costo_silla*c_s
    
    if t_c == 'F':
        descuento = total*0.20        
    elif t_c == 'N':
        if total>=10000 and total<20000:
          descuento = total*0.10
        elif total>=20000:
          descuento = total*0.15
    else:
        descuento = 0
    
    total = costo_silla*c_s
    print('El precio antes de descuento es: ', total)
    
    print('La cantidad del descuento a aplicar es:',descuento)
    
    total = total - descuento
    print('El total a pagar ya con descuento es:',round(total))
    #FIN DE LA FUNCIÓN

           
print(" * * * * * Bienvenido a la tiendita de Sillas Rancho Grande  * * * * \n")
print(" - - - Tenemos estos tipos de sillas - - -")
print("\t [B] Básica    $700.00 c/u")
print("\t [E] Estándar  $900.00 c/u")
print("\t [L] De Lujo $1,500.00 c/u")
print("")
t_silla = str(input("Indica la letra del tipo de silla que deseas comprar: "))

print(" \n - - - Tipos de Clientes - - -")
print("\t [N] Clientes Normales")
print("\t [F] Clientes Frecuentes")
print("")
t_cliente = str(input("Indica la letra de tu tipo de cliente: "))
print("")
cant_sillas = int(input("¿Cuántas sillas vas a comprar? "))
print("")
calculo_total(t_silla,t_cliente,cant_sillas)


