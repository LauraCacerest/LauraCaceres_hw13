import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

#Retorna la lista doors de manera desordena
def sort_doors():
    doors= ['goat','goat','car']
    np.random.shuffle (doors)
    return doors

print sort_doors()

#Retorna un numero aleatorio entre 0,1 o 2
#Simulando la eleccion del participante
def choose_door():
    numero=[0,1,2]
    lc=np.random.choice(numero)

    return lc
print choose_door()

#Monty Hall revela en que lugar hay una cabra
def reveal_door(lista,choice):

    for i in range(len(lista)):
            if(i!=choice) and (lista[i]== 'goat'):
                lista[i]='GOAT_MONTY'
            return lista

print reveal_door(sort_doors,reveal_door)

#  Se revelan todas la puertas

def finish_game(lista,choice,change):
    if(change == False):

        return lista [choice]

    else:

        for i in range(len(lista)):
            if (i!=change) and (lista[i]!= 'GOAT_MONTY'):
                return lista[i]

print finish_game(sort_doors,choose_door,True)

#Simulacion muchos escenarios de juego
lista_true=[]
for i in range (99):
    lc=sort_doors()
    l=choose_door()
    reveal_door(lc,l)

    lc=finish_game(lc,l,False)
