import math
def main():
    #escribe tu código abajo de esta línea
    a = float(input('Area a pintar en metros: '))
    b = float(input('Rendimiento (m2/l): '))
    x = a/b
    print('Litros a comprar: '+ str(int(math.ceil(x))))
    
if __name__ == '__main__':
    main()
