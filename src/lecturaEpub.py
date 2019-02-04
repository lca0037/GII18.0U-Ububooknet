# -*- coding: utf-8 -*-
"""
Clase para obtener el texto de los epub

@author: luism
"""

from bs4 import BeautifulSoup
import zipfile
import re

class lecturaEpub:
    
    def __init__(self,fichero):
        self.fich = fichero
        self.epub = zipfile.ZipFile(self.fich)
        self.orden = list()
#        print(self.epub.namelist())
    
    def obtenerOrdenLectura(self):
        container = self.epub.read('META-INF/container.xml')
        conta = BeautifulSoup(container, "xml")
        for link in conta.find_all('rootfile'):
            content = link.get('full-path')
        carp = re.compile('.*/')
        d = carp.match(content)
        if(d!=None):
            d = d.group()
        else:
            d = ''
            
        content = self.epub.read(content)
        conte = BeautifulSoup(content, "xml")
#        print(conte)
        ordenid = list()
        
        for link in conte.find_all('spine', limit = 1):
            for l2 in link.find_all('itemref'):
                ordenid.append(l2.get('idref'))
        for idr in ordenid:
            for idr2 in conte.find_all(id=idr, limit = 1):
                self.orden.append(d + idr2.get('href'))
    
    def siguienteArchivo(self):
        for a in self.orden:
            print(a)
            txt = ''
            seccion = self.epub.read(a)
            sect = BeautifulSoup(seccion, "xml")
            for s in sect.find_all('p'):
                txt += s.get_text()
            
            yield txt


#fich = '../tst/epubPruebas.epub'
#
#if(zipfile.is_zipfile(fich)):
#    l = lecturaEpub(fich)
#    l.obtenerOrdenLectura()
#    it = l.siguienteArchivo()
#    print(next(it))
#    print(next(it))
