import numpy as np

# Criar um array 2D (matriz) a partir de uma lista de listas
dados = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Array 2D:\n", dados)

# Média por coluna (axis=0) e por linha (axis=1)
media_colunas = np.mean(dados, axis=0)
media_linhas = np.mean(dados, axis=1)
