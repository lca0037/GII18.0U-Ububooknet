# -*- coding: utf-8 -*-
"""
Test unitarios sobre el código implementado

@author: Luis Miguel Cabrejas Arce
"""


#import sys
#sys.path.append('../src/')
import unittest
from src import modelo
from src import pospersonajes as pp
from src import lecturaEpub as lec

#print(sys.path)
m = modelo.modelo()
poslex = pp.pospersonajes(m)

class testUnitarios(unittest.TestCase):
    
    def __init__(self,*args, **kwargs):
        super(testUnitarios, self).__init__(*args, **kwargs)
        m.obtTextoEpub(r"C:\Users\luism\Desktop\Ubu\TFG\Repositorio\GII18.0U-Ububooknet\tst\epubPruebas.epub")
        m.vaciarDiccionario()
        m.crearDict()
    
    '''
    Se pone el número del test indicando el orden en el que se ejecutan debido a ser la solución
    más sencilla que se ha encontrado al problema que consiste en que los test
    se ejecutan en orden alfabético y no en el orden en el que están definidos
    '''
    
    def test_01_LecturaEpub(self):
        res = {0:['Pedro Pérez'], 1:['Josema'], 2:['Pedro'], 3:['Pedro Rodríguez'], 4:['Ana']}
        self.comprobarPersonajes(res)

    def test_02_AnadirPersonaje(self):
        m.anadirPersonaje('Andrea')
        res = {0:['Pedro Pérez'], 1:['Josema'], 2:['Pedro'], 3:['Pedro Rodríguez'], 4:['Ana'], 5:['Andrea']}
        self.comprobarPersonajes(res)

    def test_03_EliminarPersonaje(self):
        m.eliminarPersonaje(1)
        res = {0:['Pedro Pérez'], 2:['Pedro'], 3:['Pedro Rodríguez'], 4:['Ana'], 5:['Andrea']}
        self.comprobarPersonajes(res)

    def test_04_JuntarPersonajes(self):
        m.juntarPersonajes(3,2)
        res = {0:['Pedro Pérez'], 3:['Pedro Rodríguez', 'Pedro'], 4:['Ana'], 5:['Andrea']}
        self.comprobarPersonajes(res)

    def test_05_anadirReferenciaAPersonaje(self):
        m.anadirReferenciaPersonaje(0,'peperez')
        res = {0:['Pedro Pérez','peperez'], 3:['Pedro Rodríguez', 'Pedro'], 4:['Ana'], 5:['Andrea']}
        self.comprobarPersonajes(res)

    def test_06_eliminarReferenciaAPersonaje(self):
        m.eliminarReferenciaPersonaje(4,'Ana')
        res = {0:['Pedro Pérez','peperez'], 3:['Pedro Rodríguez', 'Pedro'], 5:['Andrea']}
        self.comprobarPersonajes(res)

    def test_07_AnadirJuntarPersonajes(self):
        m.anadirPersonaje('Andrea')
        res = {0:['Pedro Pérez','peperez'], 3:['Pedro Rodríguez', 'Pedro'], 5:['Andrea'], 6:['Andrea']}
        self.comprobarPersonajes(res)
        m.juntarPersonajes(5,6)
        res = {0:['Pedro Pérez','peperez'], 3:['Pedro Rodríguez', 'Pedro'], 5:['Andrea']}
        self.comprobarPersonajes(res)

    def comprobarPersonajes(self, res):
        obt = m.getPersonajes()
        self.assertEqual(len(res),len(obt))
        for k,j in zip(res.keys(),obt.keys()):
            per = obt[j].getPersonaje()
            self.assertEqual(k,j)
            self.assertEqual(len(per),len(res[k]))
            i = 0
            for sk, sj in zip(res[k][0],per.keys()):
                self.assertEqual(sk,res[k][0][i])
                i+=1

    def test_08_leerEpub(self):
        txt = list()
        txt.append('')
        texto = 'Esto es un documento de pruebas para comprobar que se obtienen'
        texto += ' bien las palabras en mayúsculas. Felipe, esto es texto de '
        texto += 'relleno Pedro Pérez, Josema esto es más texto de relleno para'
        texto += ' poder hacer pruebas Pedro esto sigue siendo relleno Pedro '
        texto += 'Rodríguez, Pedro, texto de relleno. María se fue a poner más '
        texto += 'texto de relleno. Pedro Pérez esto como no sigue siendo texto'
        texto += ' de pruebas Ana.'
        txt.append(texto)
        l = lec.lecturaEpub('tst/epubPruebas.epub')
        it = l.siguienteArchivo()
        for i in txt:
            self.assertEqual(i,next(it))

    def test_09_getDictParsear(self):
        m.anadirPersonaje('Pedro')
        res = ['Pedro Pérez', 'peperez', 'Pedro Rodríguez', 'Pedro', 'Andrea']
        obt = m.getDictParsear()
        self.assertEqual(len(res),len(obt))
        for i in range(len(res)):
            self.assertEqual(res[i],obt[i])

    def test_10_posPalabrasDict(self):
        m.vaciarDiccionario()
        m.crearDict()
        m.anadirPersonaje('María')
        m.anadirPersonaje('relleno')
        m.obtenerPosPers()
        res = {'Pedro Pérez': [23, 54], 'Josema': [24], 'Pedro': [35, 41], 'Pedro Rodríguez': [40], 'Ana': [63], 'María': [45], 'relleno': [22, 30, 39, 44, 53]}
        x = m.getPersonajes()
        for i in x.keys():
            pers = x[i].getPersonaje()
            for n in pers.keys():
                self.assertEqual(pers[n],res[n])

    def test_11_esSubcadena(self):
        l = ["Alabardero", "Ala", "Alto", "Baje", "Asta", "Corzo", "lata"]
        res1 = ['Alabardero', 'Ala', 'Alto']
        res2 = ['lata']
        res3 = []
        self.assertEqual(res1,poslex.esSubcadena("Al",l))
        self.assertEqual(res2,poslex.esSubcadena("la",l))
        self.assertEqual(res3,poslex.esSubcadena("li",l))
        
    def test_12_juntarListas(self):
        m.juntarPersonajes(0,2)
        m.juntarPosiciones()
        res = {0: [23, 35, 41, 54], 1: [24], 3: [40], 4: [63], 5: [45], 6: [22, 30, 39, 44, 53]}
        x = m.getPersonajes()
        for i in x.keys():
            self.assertEqual(res[i],x[i].getPosicionPers())
            
    def test_13_matrizAdyacencia(self):
        res = [[0,1,2,0,1,6],[1,0,0,0,0,1],[2,0,0,0,1,2],[0,0,0,0,0,0],[1,0,1,0,0,1],[6,1,2,0,1,0]]
        obt = m.getMatrizAdyacencia(5).tolist()
        self.assertEqual(res,obt)
            
if __name__ == '__main__':
    unittest.main()