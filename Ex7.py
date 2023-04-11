import numpy as np


def get_max(matriz):
    maximo = float('-inf') # Inicializa com um valor muito pequeno
    for linha in matriz:
        for valor in linha:
            if valor > maximo:
                maximo = valor
    return maximo

def get_min(matriz):
    minimo = np.inf  # começa com infinito para garantir que o primeiro valor seja menor
    for linha in matriz:
        for valor in linha:
            if valor < minimo:
                minimo = valor
    return minimo


# define o tamanho da matriz
M, N = 3, 3

# gera as matrizes aleatórias de 0 a 255
matrix1 = np.random.randint(0, 256, size=(M, N))
matrix2 = np.random.randint(0, 256, size=(M, N))

# soma as matrizes
result = matrix1 + matrix2
print("Matriz 1:\n", matrix1)
print("Matriz 2:\n", matrix2)
print("Resultado A:\n", result)

result2 = result.copy()

if(np.max(result) > 255):
    result2[result > 255] = (255/(get_max(result) - get_min(result))) * (result2[result > 255] - get_min(result))

print("Resultado B:\n", result2)

# verifica se ocorreu overflow
if np.max(result) > 255:
    # trata o overflow
    result[result > 255] = 255

# verifica se ocorreu underflow
if np.min(result) < 0:
    # trata o underflow
    result[result < 0] = 0

print("Resultado C:\n", result)