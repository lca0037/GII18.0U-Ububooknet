# -*- coding: utf-8 -*-

#from src import personaje
from tst import testUnitarios
from src import modelo, personaje, vista
import unittest
import time
#runner = unittest.TextTestRunner()
#result = runner.run(unittest.makeSuite(testUnitarios.testUnitarios))
vista.app.run()
#m = modelo.modelo.getInstance()
#m.vaciarDiccionario()
#start = time.time()
#m.obtTextoEpub(r"C:\Users\luism\Desktop\Ubu\TFG\Epubs\Harry Potter y el Caliz de Fuego - J. K. Rowling.epub")
#print(time.time()-start)
#m.crearDict()
#print(len(m.getPersonajes().keys()))
##print(time.time()-start)
##for i in m.getPersonajes().keys():
##    print(m.getPersonajes()[i].getPersonaje())
##print(time.time()-start)
##m.obtenerPosPers()
##print(time.time()-start)
##m.juntarPosiciones()
##print(time.time()-start)
#print(m.generarGrafo(30,10))
#print(time.time()-start)
#print(m.visualizar())