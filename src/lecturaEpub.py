# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import zipfile
import re

"""
Clase para obtener el texto de los epub

@author: Luis Miguel Cabrejas
"""
class lecturaEpub:
    
    '''
    Constructor de la clase
    '''
    def __init__(self,fichero):
        self.fich = fichero
        self.epub = zipfile.ZipFile(self.fich)
        self.__orden = list()
#        print(self.epub.namelist())
    
    '''
    Obtiene el orden de lectura en el que se deben leer los ficheros de 
    un archivo epub
    '''
    def __obtenerOrdenLectura(self):
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
                self.__orden.append(d + idr2.get('href'))
    
    '''
    Iterador que devuelve el texto de cada fichero a leer del epub
    '''
    def siguienteArchivo(self):
        self.__obtenerOrdenLectura()
        for a in self.__orden:
            txt = ''
            seccion = self.epub.read(a)
            sect = BeautifulSoup(seccion, "xml")
            for s in sect.find_all('p'):
                txt = txt + s.get_text()+ ". "
            yield txt

