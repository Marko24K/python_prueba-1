def main():
    def area (r):
        return ((r**2) * 3.14)
    
    def volumen (r, h):
        return (r * h)
     
    x=int(input("Ingrese el radio del circulo a calular: "))
    print("El área del circulo es: " + str(area(x)))
    h=int(input("Para calcular el volumen de un cilindro se usara la misma area del circulo, ingrese su altura: "))
    print("El volumen del cilidro es: "+ str(volumen(area(x), h)))
    
if __name__ == '__main__':
    main() 

    