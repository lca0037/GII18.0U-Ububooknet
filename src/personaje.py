# -*- coding: utf-8 -*-
"""
Clase que contiene información sobre cada personaje

@author: luism
"""


class personaje:
    
    def __init__(self,nom,apariciones):
        self.nombres= dict()
        self.nombres[nom] = apariciones
        
    def getPersonaje(self):
        return self.nombres
    
#    def keys(self):
#        return self.nombres.keys()