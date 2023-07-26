def main():
    empleado=str(input("¿Que empleado desea evaluar?: "))
    puntuacion=float(input("Ingrese la puntuacion (0.0, 0.4, 0.6 o mas): "))
    if(puntuacion == 0.0):
        print("El empleado "+ empleado + " obtuvo de beneficio de " + str(puntuacion * 2400) +"€")
    elif(puntuacion == 0.4):
        print("El empleado "+ empleado + " obtuvo de beneficio de " + str(puntuacion * 2400) +"€")
    elif(puntuacion >= 0.6):
        print("El empleado "+ empleado + " obtuvo de beneficio de " + str(puntuacion * 2400) +"€")
    else:
        print("solo puntuaciones de (0.0, 0.4, 0.6 o mas) no valores intermedios entre las cifras mencionadas.")
    
if __name__ == '__main__': 
    main()