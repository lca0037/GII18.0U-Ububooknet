# -*- coding: utf-8 -*-
import csv
from src import personaje as p

class lectorcsv:
    
    def __init__(self,m):
        self.__modelo = m
        
    def importDict(self, fichero):
        i = 0
        pers = self.__modelo.getPersonajes()
        with open(fichero, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',',skipinitialspace=True)
            for row in spamreader:
                if (i%2 ==0):
                    i+=1
                    actual = row[0]
                    pers[actual] = p.personaje()
                else:
                    i+=1
                    for n in row:
                        self.__modelo.anadirReferenciaPersonaje(actual,n)
        print(pers)
    
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