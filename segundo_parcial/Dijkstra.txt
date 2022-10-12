from cProfile import label
from cmath import nan
from hashlib import new
from nntplib import ArticleInfo

import numpy as np

caminos = []
pisados = []

matriz = [
    [0, 10, 3, 0, 0],
    [10, 0, 2, 1.5, 0],
    [3, 2, 0, 1, 6],
    [0, 1.5, 1, 0, 5],
    [0, 0, 6, 5, 0]
];


def dijkstra(punto=nan, final=nan, camino=[], contador=nan, pisadas=[]):
    print(contador)
    if (punto == final):
        camino.append(punto)
        caminos.append(camino)
        return;

    if contador % 2 == 1:
        newcontador = contador + 1;
        # incremento en y
        pisadas.append(punto)
        for i in range(len(matriz)):
            if (matriz[punto][i] != 0) and i not in pisadas:
                print("entro arriba con ", i)
                print("pisadas: ", pisadas)
                newcomino = camino.copy()
                newcomino.append(punto)

                dijkstra(punto=i, final=final, camino=newcomino, contador=newcontador, pisadas=pisadas);
            else:
                if (matriz[punto][i] != 0):
                    print("se encontro en pisadas en el punto", i, pisadas, contador)

    else:
        # incremento en x

        newcontador = contador + 1;
        pisadas.append(punto)
        for i in range(len(matriz[0])):

            if (matriz[i][punto] != 0) and i not in pisadas:
                print("entro abajo con ", i)
                print("pisadas: ", pisadas)
                newcomino = camino.copy()
                newcomino.append(punto)

                dijkstra(punto=i, final=final, camino=newcomino, contador=newcontador, pisadas=pisadas);
            else:
                if (matriz[i][punto] != 0):
                    print("se encontro en pisadas en el punto", i, pisadas, contador)

    print("termine la funcion con el punto ", punto)


dijkstra(punto=1, final=4, contador=1)

print(caminos)