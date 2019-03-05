# -*- coding: utf-8 -*-
import csv

class lectorcsv:
    
    def __init__(self,fichero):
        self.fichero = fichero
        
    
    def importDict(self):
        i = 0
        pers = dict()
        with open(self.fichero, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',',skipinitialspace=True)
            for row in spamreader:
                if (i%2 ==0):
                    i+=1
                    actual = row[0]
                    pers[actual] = dict()
                else:
                    i+=1
                    for n in row:
                        pers[actual][n] = 0
        print(pers)
    
    def exportDict(self):
        print('Metodo sin implementar')

lcsv = lectorcsv('PruebasImpExp.csv')
lcsv.importDict()