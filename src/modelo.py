# -*- coding: utf-8 -*-
"""
Clase con la que la vista interactua

@author: luism
"""

import ply.lex as lex
from src import personaje as p
from src import creadict as cd
import matplotlib.pyplot as plt
import numpy as np

class modelo:
    
    def __init__(self):
        self.texto = 'Esto es un documento de pruebas para comprobar que se obtienen'
        self.texto += ' bien las palabras en mayúsculas. Felipe, esto es texto de '
        self.texto += 'relleno Pedro Pérez, Josema esto es más texto de relleno para'
        self.texto += ' poder hacer pruebas Pedro esto sigue siendo relleno Pedro '
        self.texto += 'Rodríguez, Pedro, texto de relleno. María se fue a poner más '
        self.texto += 'texto de relleno. Pedro Pérez esto como no sigue siendo texto'
        self.texto += ' de pruebas Ana.'
        self.personajes= dict()
        self.numpers = 0
        self.sigid = 0
     
    def crearDict(self):
        creard = cd.creadict()
        p,n = creard.crearDict(self.texto)
        self.personajes = p
        self.numpers = n
        self.sigid = n
        
    def getDictParsear(self):
        l = list()
        for i in self.personajes.keys():
            for n in self.personajes[i].getPersonaje():
                if(n not in l):
                    l.append(n)
        return l
    
    def esSubcadena(self,st,lista):
        l = list()
        aux = True
        for pal in lista:
            for i in range(len(st)):
                if(st[i] != pal[i]):
                    aux = False
                    break
            if(aux):
                l.append(pal)
            else:
                aux = True
        return l
    
    def getPersonajes(self):
        return self.personajes
    
    def histogramaPersonajes(self):
        x = list()
        y = list()
        for k in self.personajes.keys():
            p = self.personajes[k].getPersonaje()
            for sk in p.keys():
                x.append(sk)
                y.append(p[sk])
        tam = np.arange(self.numpers)
        plt.title('Frecuencia personajes')
        plt.xlabel('Nombre')
        plt.ylabel('Apariciones')
        plt.bar(tam,height=y)
        plt.xticks(tam,x)
    
    def anadirPersonaje(self, pers):
        self.personajes[self.numpers] = p.personaje(pers,0)
        self.numpers+=1
        
    def eliminarPersonaje(self, idPersonaje):
        if(idPersonaje in self.personajes):
            del self.personajes[idPersonaje]
        
    def juntarPersonajes(self, idPersonaje1, idPersonaje2):
        if(idPersonaje1 in self.personajes and idPersonaje2 in self.personajes):
            pers1 = self.personajes[idPersonaje1].getPersonaje()
            pers2 = self.personajes[idPersonaje2].getPersonaje()
            for k in pers2.keys():
                if k in pers1.keys():
                    pers1[k]+=pers2[k]
                else:
                    pers1[k]=pers2[k]
            self.eliminarPersonaje(idPersonaje2)
            
    def anadirReferenciaPersonaje(self,idp,ref):
        if(idp in self.personajes.keys()):
            p = self.personajes[idp].getPersonaje()
            if(ref not in p.keys()):
                p[ref]=0
        
    def eliminarReferenciaPersonaje(self,idp,ref):
        if(idp in self.personajes.keys()):
            p = self.personajes[idp].getPersonaje()
            if(ref in p.keys()):
                if (len(p)>1):
                    del p[ref]
                else:
                    del self.personajes[idp]
