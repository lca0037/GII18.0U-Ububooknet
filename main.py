# -*- coding: utf-8 -*-

#from src import personaje
from tst import testUnitarios
from src import modelo, personaje, vista
import unittest
import time

#testUnitarios.testUnitarios()
#testUnitarios.unittest.main()

#runner = unittest.TextTestRunner()
#result = runner.run(unittest.makeSuite(testUnitarios.testUnitarios))
vista.app.run()
#
#m = modelo.modelo.getInstance()
#m.vaciarDiccionario()
#start = time.time()
#m.obtTextoEpub(r"C:\Users\luism\Desktop\Ubu\TFG\Epubs\Harry Potter y el Caliz de Fuego - J. K. Rowling.epub")
#print(time.time()-start)
#m.crearDict()
#print(time.time()-start)
#m.obtenerPosPers()
#print(time.time()-start)
#m.juntarPosiciones()
#print(time.time()-start)
#print(m.getMatrizAdyacencia(20).tolist())
#print(time.time()-start)