import random
import os

def greeadySearchWay(configOriginal):
    print("Hello")

def getChooseOrRandom(prompt, start, random_limit, text1, text2):
    choose = input(prompt)
    if choose.isdigit():
        n = get_integer_input(text1)
        m = get_integer_input(text2)
    else:
        n = random.randint(start, random_limit)
        m = random.randint(start, random_limit)
    return n, m

def manualConfig(remindConfig):
    choose = input("Escribe un numero si quieres escojer las dimeciones del laberinto, de lo contrario sera aleatorio")
    n,m=getChooseOrRandom(choose,1, 10, "Proporciona n: ", "Proporciona m: ")
    remindConfig.append(n)
    remindConfig.append(m)
    tempMaze=create_matrix(n,m)
    print("Así es como quedo:")
    print_matrix(tempMaze)
    choose = input("Escribe un numero si quieres escojer el inicio y la meta, de lo contrario sera aleatorio")
    n,m = getChooseOrRandom(choose,0,10, "Proporciona x: ", "Proporciona y: ")
    remindConfig.append(n)
    remindConfig.append(m)
    tempMaze[n][m]=1
    n,m = getChooseOrRandom(choose,0,10, "Proporciona x: ", "Proporciona y: ")
    remindConfig.append(n)
    remindConfig.append(m)
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
            return int(n)
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
            if len(config) ==6:
                maze =create_matrix(config[0],config[1])
                maze[int(config[2])][int(config[3])]=1
                maze[int(config[4])][int(config[5])]=2

    else:
        print(f"El archivo '{d_configuration}' no se encontró en el directorio actual.\n Realiza la configuracion manual.")
        maze, config=manualConfig(config)
        greeadySearchWay(config)
    print_matrix(maze)

if __name__ == "__main__":
    main()