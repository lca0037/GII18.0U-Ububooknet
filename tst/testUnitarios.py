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
    
    #Se pone el número del test indicando el orden en el que se ejecutan debido a ser la solución
    #más sencilla que se ha encontrado al problema que consiste en que los test
    #se ejecutan en orden alfabético y no en el orden en el que están definidos
    
    def test_01_LecturaEpub(self):
        res = {0:{'Pedro Pérez': 2}, 1:{'Josema':1}, 2:{'Pedro':2}, 3:{'Pedro Rodríguez':1}, 4:{'Ana':1}}
        self.comprobarPersonajes(res)
    
    def test_02_AnadirPersonaje(self):
        m.anadirPersonaje('Andrea')
        res = {0:{'Pedro Pérez': 2}, 1:{'Josema':1}, 2:{'Pedro':2}, 3:{'Pedro Rodríguez':1}, 4:{'Ana':1}, 5:{'Andrea':0}}
        self.comprobarPersonajes(res)
        
    def test_03_EliminarPersonaje(self):
        m.eliminarPersonaje(1)
        res = {0:{'Pedro Pérez': 2}, 2:{'Pedro':2}, 3:{'Pedro Rodríguez':1}, 4:{'Ana':1}, 5:{'Andrea':0}}
        self.comprobarPersonajes(res)
            
    def test_04_JuntarPersonajes(self):
        m.juntarPersonajes(3,2)
        res = {0:{'Pedro Pérez': 2}, 3:{'Pedro Rodríguez':1, 'Pedro':2}, 4:{'Ana':1}, 5:{'Andrea':0}}
        self.comprobarPersonajes(res)
        
    def comprobarPersonajes(self, res):
        obt = m.getPersonajes()
        i = 0
        self.assertEqual(len(res),len(obt))
        for k,j in zip(res.keys(),obt.keys()):
            per = obt[j].getPersonaje()
            self.assertEqual(k,j)
            self.assertEqual(len(per),len(res[k]))
            for sk, sj in zip(res[k].keys(),per.keys()):
                self.assertEqual(per[sj],res[k][sk])
            i+=1
            
if __name__ == '__main__':
    unittest.main()