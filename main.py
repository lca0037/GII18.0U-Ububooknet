# -*- coding: utf-8 -*-

#from src import personaje
from tst import testUnitarios
from src import modelo, personaje, vista
import unittest
import time
#runner = unittest.TextTestRunner()
#result = runner.run(unittest.makeSuite(testUnitarios.testUnitarios))
vista.app.run(debug=True)
#m = modelo.modelo.getInstance()
#m.vaciarDiccionario()
#start = time.time()
#m.setFichero(r"C:\Users\luism\Desktop\Ubu\TFG\Epubs\Harry Potter y el Caliz de Fuego - J. K. Rowling.epub")
#m.obtTextoEpub()
#print(time.time()-start)
#m.crearDict()
#m.importDict(r"C:\Users\luism\Desktop\Ubu\TFG\Epubs\DiccionarioPersonajes.csv")
#m.juntarListPersonajes(['Harry','Potter','Harry Potter'])
#print(len(m.getPersonajes().keys()))
#print(time.time()-start)
#m.obtenerPosPers()
#m.juntarPosiciones()
#for i in m.getPersonajes().keys():
#    print(m.getPersonajes()[i].getPersonaje(), m.getPersonajes()[i].lennombres)
#    print(m.getPersonajes()[i].getPosicionPers())
#    print(m.getPersonajes()[i].getNumApariciones())
#m.generarGrafo(3000,10,True)
#print(m.getMatrizAdyacencia())
#m.generarGrafo(3000,10,False)
#print(m.getMatrizAdyacencia())
#print(m.getTexto())
##print(time.time()-start)
##m.obtenerPosPers()
##print(time.time()-start)
##m.juntarPosiciones()
##print(time.time()-start)
#print(m.generarGrafo(30,10))
#print(time.time()-start)
#print(m.visualizar())
