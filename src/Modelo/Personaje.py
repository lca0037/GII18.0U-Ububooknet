# -*- coding: utf-8 -*-

"""
Clase que contiene información sobre cada personaje

@author: luism
"""
class Personaje:
    
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
        for k in self.__nombres.keys():
            if k not in self.lennombres:
                return self.__numapar,False
        return self.__numapar,True
    
    def sumNumApariciones(self,apar):
        self.__numapar += apar
        
    def resNumApariciones(self,apar):
        self.__numapar -= apar