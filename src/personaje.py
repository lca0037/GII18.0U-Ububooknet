# -*- coding: utf-8 -*-

"""
Clase que contiene información sobre cada personaje

@author: luism
"""
class personaje:
    
    '''
    Constructor de la clase
    '''
    def __init__(self):
        self.__nombres= dict()
        self.__pospers = list()
        
    '''
    Devuelve la lista de nombres para ese personaje
    '''
    def getPersonaje(self):
        return self.__nombres
    
    '''
    Devuelve la lista de todas las posiciones en las que sale un nombre de ese
    personaje
    '''
    def getPosicionPers(self):
        return self.__pospers
    
    '''
    Devuelve el número de apariciones del personaje
    '''
    def getNumApariciones(self):
        return len(self.__pospers)
    