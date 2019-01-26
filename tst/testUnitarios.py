# -*- coding: utf-8 -*-
"""
Test unitarios sobre el código implementado

@author: Luis Miguel Cabrejas Arce
"""

import unittest
import modelo as mod

m = mod.modelo();
m.leerEpub('epubPruebas.epub')

class testUnitarios(unittest.TestCase):
    
    def testLecturaEpub(self):
        res = [['Pedro Pérez', 2], ['Josema',1], ['Pedro',1], ['Pedro Rodríguez',1], ['Ana',1]]
        self.comprobarPersonajes(res)
    
    def testAnadirPersonaje(self):
        m.anadirPersonaje('Andrea')
        res = [['Pedro Pérez', 2], ['Josema',1], ['Pedro',1], ['Pedro Rodríguez',1], ['Ana',1], ['Andrea',0]]
        self.comprobarPersonajes(res)
        
    def testEliminarPersonaje(self):
        m.eliminarPersonaje(1)
        res = [['Pedro Pérez', 2], ['Pedro',1], ['Pedro Rodríguez',1], ['Ana',1], ['Andrea',0]]
        self.comprobarPersonajes(res)
            
    def testJuntarPersonajes(self):
        m.juntarPersonajes(3,2)
        res = [['Pedro Pérez', 2], ['Pedro Rodríguez',1], ['Pedro',1], ['Ana',1], ['Andrea',0]]
        self.comprobarPersonajes(res)
        
    def comprobarPersonajes(self, res):
        obt = m.getPersonajes()
        i = 0
        for k in obt.keys():
            for sk in obt[k].keys():
                self.assertEqual(sk,res[i][0])
                self.assertEqual(obt[k][sk],res[i][1])
            i+=1