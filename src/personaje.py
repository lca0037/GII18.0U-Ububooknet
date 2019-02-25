# -*- coding: utf-8 -*-
"""
Clase que contiene información sobre cada personaje

@author: luism
"""


class personaje:
    
    def __init__(self,nom,apariciones):
        self.nombres= dict()
        self.nombres[nom] = apariciones
        self.pospers = list()
        
    def getPersonaje(self):
        return self.nombres
    
    def getPosicionPers(self):
        return self.pospers
    