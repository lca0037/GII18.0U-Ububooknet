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
        self.__pospers = dict()
        self.lennombres = dict()
        self.__numapar = 0
        
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
    
    def setPosicionPers(self,pospers):
        self.__pospers = pospers
    
    '''
    Devuelve el número de apariciones del personaje
    '''
    def getNumApariciones(self):
        return self.__numapar
    
    def sumNumApariciones(self,apar):
        self.__numapar += apar
    