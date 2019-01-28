# -*- coding: utf-8 -*-
"""
Test unitarios sobre el código implementado

@author: Luis Miguel Cabrejas Arce
"""


import sys
sys.path.append('../src/')
import unittest
import modelo as mod



#print(sys.path)
m = mod.modelo();
m.crearDiccionario()
class testUnitarios(unittest.TestCase):
    
    def testLecturaEpub(self):
        res = {0:{'Pedro Pérez': 2}, 1:{'Josema':1}, 2:{'Pedro':2}, 3:{'Pedro Rodríguez':1}, 4:{'Ana':1}}
        self.comprobarPersonajes(res)
    
    def testAnadirPersonaje(self):
        m.anadirPersonaje('Andrea')
        res = {0:{'Pedro Pérez': 2}, 1:{'Josema':1}, 2:{'Pedro':2}, 3:{'Pedro Rodríguez':1}, 4:{'Ana':1}, 5:{'Andrea':0}}
        self.comprobarPersonajes(res)
        
    def testEliminarPersonaje(self):
        m.eliminarPersonaje(1)
        res = {0:{'Pedro Pérez': 2}, 2:{'Pedro':2}, 3:{'Pedro Rodríguez':1}, 4:{'Ana':1}, 5:{'Andrea':0}}
        self.comprobarPersonajes(res)
            
    def testJuntarPersonajes(self):
        m.juntarPersonajes(3,2)
        res = {0:{'Pedro Pérez': 2}, 3:{'Pedro Rodríguez':1, 'Pedro':2}, 4:{'Ana':1}, 5:{'Andrea':0}}
        self.comprobarPersonajes(res)
        
    def comprobarPersonajes(self, res):
        obt = m.getPersonajes()
        i = 0
        for k in res.keys():
            per = obt[k].getPersonaje()
            for sk in res[k].keys():
                self.assertEqual(per[sk],res[k][sk])
            i+=1
            
if __name__ == '__main__':
    unittest.main()