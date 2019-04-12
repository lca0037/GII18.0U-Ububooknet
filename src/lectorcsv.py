# -*- coding: utf-8 -*-
import csv
from src import personaje as p

"""
Clase para importar y exportar diccionarios de personajes

@author: Luis Miguel Cabrejas Arce
"""
class lectorcsv:
    
    '''
    Constructor de la clase
    '''
    def __init__(self,m):
        self.__modelo = m
       
    '''
    Importa un diccionario de personajes que tenga una estructura predeterminada
    '''
    def importDict(self, fichero):
        i = 0
        pers = self.__modelo.getPersonajes()
        with open(fichero, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',',skipinitialspace=True)
            for row in spamreader:
                if (i%2 ==0):
                    i+=1
                    actual = row[0]
                    self.__modelo.anadirPersonaje(actual,actual)
                else:
                    i+=1
                    for n in row:
                        self.__modelo.anadirReferenciaPersonaje(actual,n)
    
    '''
    Exporta el diccionario de personajes actual a un fichero csv con una estructura
    igual a la de los ficheros de importación
    '''
    def exportDict(self, fichero):
        pers = self.__modelo.getPersonajes()
        with open(fichero, mode='w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for persk in pers.keys():
                spamwriter.writerow([persk])
                spamwriter.writerow(pers[persk].getPersonaje().keys())


#lcsv = lectorcsv('PruebasImpExp.csv')
#lcsv.importDict()
#
#lcsv2 = lectorcsv('dictexportado.csv')
#lcsv2.exportDict()
#lcsv2.importDict()