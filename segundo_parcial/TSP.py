from cProfile import label
from cmath import nan
from curses import init_color
from hashlib import new
from nntplib import ArticleInfo
#import networkx as nx
#import graphviz
import numpy as np

#G = nx.Graph()

nodos_por_recorrer=[]
caminos=[]


matriz=[
    [0, 10,  3,  7, 50],
    [10, 0, 20,  8, 60],
    [3, 20,  0, 30,  7],
    [7,  8, 30,  0, 40],
    [50,60,  7, 40,  0]
];

for i in range(len(matriz)):
    nodos_por_recorrer.append(i)



def tsp(punto=nan,inicio=nan, camino=[], contador=nan,pisadas=[],por_recorrer=[] ,peso=0):
    pisadas.append(punto)
    print(camino,por_recorrer)
    if (sorted(pisadas)==sorted(por_recorrer)):
        # camino.append(punto)
        newpisadas=pisadas.copy()
        newpeso=peso+matriz[punto][inicio]
        camino.append(peso)
        caminos.append(camino)
    
        return;
  
   
    if contador%2==1:
        newcontador=contador+1;
        #incremento en y
        
        for i in range (len(matriz)):
            if(matriz[punto][i]!=0) and i not in pisadas:
           
                newcomino=camino.copy()
                newcomino.append(punto)
                newpisadas=pisadas.copy()
                newpeso=peso+matriz[punto][i]
                
                tsp(punto=i,camino=newcomino,inicio=inicio,contador=newcontador,pisadas=newpisadas,por_recorrer=por_recorrer, peso=newpeso);
           
        
    else:
        #incremento en x
        
        newcontador=contador+1;

        for i in range (len(matriz[0])):
            
            if(matriz[i][punto]!=0)  and i not in pisadas:

                newcomino=camino.copy()
                newcomino.append(punto)
                newpisadas=pisadas.copy()
                newpeso=peso+matriz[i][punto]
           
                tsp (punto=i,camino=newcomino,inicio=inicio,contador=newcontador,pisadas=newpisadas,por_recorrer=por_recorrer, peso=newpeso);
            

tsp(punto=0,por_recorrer=nodos_por_recorrer,contador=1)
caminos