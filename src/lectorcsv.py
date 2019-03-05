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
        pers = {'Toni': {'Antonio': 0, 'Toño': 0}, 'Mar':{'Marimar': 0, 'María': 0, 'Mar':0}, 'Juan': {'Juan': 0}, 'Andrea': {'Andrea': 0}, 'Sandra': {'Sandra': 0, 'Sand': 0}}
        with open(self.fichero, mode='w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for persk in pers.keys():
                spamwriter.writerow([persk])
                spamwriter.writerow(pers[persk].keys())


#lcsv = lectorcsv('PruebasImpExp.csv')
#lcsv.importDict()
#
#lcsv2 = lectorcsv('dictexportado.csv')
#lcsv2.exportDict()
#lcsv2.importDict()