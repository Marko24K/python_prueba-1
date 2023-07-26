def main():
    
    fecha=str(input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: "))
    fecha=fecha.replace("/", " ")    
    print("Día " + fecha[:2:])
    print("Mes"+ fecha[2:5:])
    print("Año"+ fecha[5:10:])
    
if __name__ == '__main__': 
    main()
