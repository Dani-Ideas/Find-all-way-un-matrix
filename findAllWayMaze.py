from itertools import permutations
import math as mt
import random
import os

def combination(n):
    temp=1
    for i in range(n,1,-1):
        temp*=i
    return temp

def permutationCustom(s):
    s = list(s)
    s.sort()    
    print(''.join(s))
    while True:
        m = len(s) - 2
        while m >= 0 and s[m] >= s[m + 1]:
            m -= 1
        if m < 0:
            break        
        k = len(s) - 1
        while s[k] <= s[m]:
            k -= 1
        s[m], s[k] = s[k], s[m]
        s = s[:m + 1] + s[m + 1:][::-1]
        print(''.join(s))


def greeadySearchWay(configOriginal):
    #Función para mostrar todos los posibles caminos de inicio a la meta
    """

    Al tratarse de un problema en un plano coordenado en R², con las siguientes restricciones:

    *Solo se permite moverse hacia la derecha o hacia arriba, sin desplazamientos diagonales.
    *De acuerdo con el teorema de Pitágoras, tanto la distancia como el desplazamiento serán siempre los mismos 
    independientemente del camino elegido. Sin embargo, aunque el número de movimientos hacia la derecha y hacia arriba 
    será constante, las variaciones posibles radican en el orden de los movimientos. Es decir, se mantendrá el mismo número 
    de desplazamientos hacia la derecha y hacia arriba, pero con diferentes combinaciones.

    Dado un punto de inicio (x0,y0) y un punto de meta (x1,y1):
    x (el número de movimientos hacia la derecha) = x1-x0
    y (el número de movimientos hacia arriba) = y1-y0

    Para calcular las posibles combinaciones
    """
    # Calcular el número de movimientos hacia la derecha y hacia arriba
    x = int(configOriginal[5]) - int(configOriginal[2])
    y = int(configOriginal[4]) - int(configOriginal[3])
    movimientos = ['d'+ str(i+1) for i in range(abs(x))]+ ['i'+ str(j+1) for j in range(abs(y))] 

    total= combination(len(movimientos))
    print(f"El numero total de posibles caminos es {total}, estos son:\n")
    #permutationCustom(movimientos)
    if int(configOriginal[6])==1:
        permutations(movimientos)
        verificado=mt.perm(len(movimientos),len(movimientos))
        print(f"Verificaccion de  la libreria oficial\nPosibles caminos: {verificado}\n")
        toPrint= permutations(movimientos)
        cont=0
        for perm in toPrint:
            cont+=1
            print(cont,": ",perm)

def getChooseOrRandom(prompt, start, random_limit, text1, text2,remindConfig):
    choose = input(prompt)
    if choose.isdigit():
        n = get_integer_input(text1)
        m = get_integer_input(text2)
    else:
        n = random.randint(start, random_limit)
        m = random.randint(start, random_limit)
    remindConfig.append(n)
    remindConfig.append(m)
    return n, m

def manualConfig(remindConfig):
    choose = input("Escribe un numero si quieres escojer las dimeciones del laberinto, de lo contrario sera aleatorio")
    n,m,remindConfig=getChooseOrRandom(choose,1, 10, "Proporciona n: ", "Proporciona m: ",remindConfig)
    tempMaze=create_matrix(n,m)
    choose = input("Escribe un numero si quieres escojer el inicio y la meta, de lo contrario sera aleatorio")
    n,m= getChooseOrRandom(choose,0,10, "Proporciona x: ", "Proporciona y: ",remindConfig)
    tempMaze[n][m]=1
    n,m= getChooseOrRandom(choose,0,10, "Proporciona x: ", "Proporciona y: ",remindConfig)
    tempMaze[n][m]=2
    return tempMaze , remindConfig

def print_matrix(matrix):
    #Función para imprimir la matriz.
    for row in matrix:
        print(row)

def create_matrix(n,m):
    return [[0] * int(n) for _ in range(int(m))]

def get_integer_input(prompt):
    #Función para obtener un número entero del usuario con validación.
    number = input(prompt)
    flag = True
    while flag:
        if number.isdigit():
            flag = False
            return int(number)
        else:
            print("La entrada no es un número válido. Intentalo de nuevo.")
            number = input(prompt)

def main():
    m=0
    n=0
    config = []
    configuration= "configData.txt"
    d_actual = os.path.dirname(os.path.abspath(__file__))
    d_configuration = os.path.join(d_actual, configuration)
    if os.path.isfile(d_configuration):
        with open(d_configuration, 'r') as archivo:
            for line in archivo:
                line = line.strip()
                config.append(line)
            if len(config) ==7:
                maze =create_matrix(config[0],config[1])
                maze[int(config[2])][int(config[3])]=1
                maze[int(config[4])][int(config[5])]=2

    else:
        print(f"El archivo '{d_configuration}' no se encontró en el directorio actual.\n Realiza la configuracion manual.")
        maze, config=manualConfig(config)
    print_matrix(maze)
    greeadySearchWay(config)

if __name__ == "__main__":
    main()