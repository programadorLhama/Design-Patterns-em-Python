import numpy as np

class NumpyFacade:
    def criar_array(self, lista):
        """Cria um array a partir de uma lista."""
        return np.array(lista)

    def media(self, array):
        """Calcula a média do array."""
        return np.mean(array)

    def media_with_axis(self, array, axis):
        return np.mean(array, axis=axis)

    def desvio_padrao(self, array):
        """Calcula o desvio padrão do array."""
        return np.std(array)

    def soma(self, array):
        """Calcula a soma dos elementos do array."""
        return np.sum(array)
