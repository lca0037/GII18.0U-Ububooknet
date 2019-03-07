# -*- coding: utf-8 -*-
"""
Clase que contiene información sobre cada personaje

@author: luism
"""


class personaje:
    
    def __init__(self):
        self.__nombres= dict()
        self.__pospers = list()
        
    def getPersonaje(self):
        return self.__nombres
    
    def getPosicionPers(self):
        return self.__pospers
    
    def getNumApariciones(self):
        return len(self._pospers)

    def getAnadidos(self):
        return self.__anadido
    