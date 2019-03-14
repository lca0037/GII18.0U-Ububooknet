# -*- coding: utf-8 -*-
from src import personaje as p
from src import creadict as cd
from src import pospersonajes as pp
from src import lectorcsv
from src import lecturaEpub
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import urllib
from bs4 import BeautifulSoup

"""
Clase con la que la vista interactua

@author: Luis Miguel Cabrejas
"""
class modelo:
    
    __instance = None
    '''
    Constructor de la clase
    '''
    def __init__(self):
        if modelo.__instance is not None:
            raise Exception("An instance already exists!")
        self.__texto = ''
        self.personajes= dict()
        self.numpers = 0
        self.sigid = 0
        self.__csv = lectorcsv.lectorcsv(self)
        if(modelo.__instance == None):
            modelo.__instance = self
     
    '''
    Método para obtener una instancia de la clase
    '''
    @staticmethod
    def getInstance():
        if modelo.__instance == None:
            modelo()
        return modelo.__instance
    
    '''
    Método que llama a un método para crear un diccionario automaticamente
    '''
    def crearDict(self):
        creard = cd.creadict()
        creard.crearDict(self.getTexto())
        self.sigid = self.numpers 
    
    '''
    Método que llama a un método para obtener las posiciones de los personajes
    '''
    def obtenerPosPers(self):
        posper = pp.pospersonajes()
        res = posper.obtenerPos(self.getTexto(), self.getDictParsear())
        for i in self.personajes.keys():
            pers = self.personajes[i].getPersonaje()
            for n in pers.keys():
                pers[n] = res[n]
      
    '''
    Función que genera una lista de nombres para obtener su posición en el texto
    '''          
    def getDictParsear(self):
        l = list()
        for i in self.personajes.keys():
            for n in self.personajes[i].getPersonaje():
                if(n not in l):
                    l.append(n)
        return l
    
    '''
    Funcíon que devuelve el diccionario de personajes
    '''
    def getPersonajes(self):
        return self.personajes
    
    '''
    Método que genera un histograma con los personajes
    '''
    def histogramaPersonajes(self):
        x = list()
        y = list()
        for k in self.personajes.keys():
            x.append(k)
            y.append(self.personajes[k].getNumApariciones())
        tam = np.arange(self.numpers)
        plt.title('Frecuencia personajes')
        plt.xlabel('Nombre')
        plt.ylabel('Apariciones')
        plt.bar(tam,height=y)
        plt.xticks(tam,x)
        
    '''
    Método que limpia el diccionario de personajes
    '''
    def vaciarDiccionario(self):
        self.personajes = dict()
        self.numpers = 0
        self.sigid = 0
    
    '''
    Método para añadir un personaje al diccionario de personajes
    '''
    def anadirPersonaje(self, pers):
        self.personajes[self.numpers] = p.personaje()
        self.personajes[self.numpers].getPersonaje()[pers] = list()
        self.numpers+=1
        
    '''
    Método para eliminar personajes
    '''
    def eliminarPersonaje(self, idPersonaje):
        if(idPersonaje in self.personajes):
            del self.personajes[idPersonaje]
       
    '''
    Método para juntar personajes
    '''
    def juntarPersonajes(self, idPersonaje1, idPersonaje2):
        if(idPersonaje1 in self.personajes and idPersonaje2 in self.personajes):
            pers1 = self.personajes[idPersonaje1].getPersonaje()
            pers2 = self.personajes[idPersonaje2].getPersonaje()
            for k in pers2.keys():
                if k not in pers1.keys():
                    pers1[k]=pers2[k]
            self.eliminarPersonaje(idPersonaje2)
    
    '''
    Método para añadir otro nombre para referirse a un personaje
    '''
    def anadirReferenciaPersonaje(self,idp,ref):
        if(idp in self.personajes.keys()):
            p = self.personajes[idp].getPersonaje()
            if(ref not in p.keys()):
                p[ref]= list()
    
    '''
    Método que elimina una referencia a un personaje
    '''
    def eliminarReferenciaPersonaje(self,idp,ref):
        if(idp in self.personajes.keys()):
            p = self.personajes[idp].getPersonaje()
            if(ref in p.keys()):
                if (len(p)>1):
                    del p[ref]
                else:
                    del self.personajes[idp]
    
    '''
    Método que junta las posiciones de todos los nombres de un personaje
    '''
    def juntarPosiciones(self):
        for i in self.personajes.keys():
            pers = self.personajes[i].getPersonaje()
            pos = self.personajes[i].getPosicionPers()
            for n in pers.keys():
                    i = 0
                    for j in pers[n]:
                        while(i<len(pos) and pos[i]<j):
                            i+=1
                        pos.insert(i,j)
        
    '''
    Método para obtener una matriz de adyacencia de las relaciones entre los personajes
    '''
    def getMatrizAdyacencia(self,rango):
        persk = list(self.personajes.keys())
        tam = len(persk)
        G = nx.Graph()
        for i in range(tam):
            for j in range(i+1,tam):
                peso = 0
                for posi in self.personajes[persk[i]].getPosicionPers():
                    for posj in self.personajes[persk[j]].getPosicionPers():
                        if(posj>=(posi-rango)):
                            if(posj<=(posi+rango)):
                                peso+=1
                            else:
                                break
                G.add_edge(persk[i],persk[j],weight=peso)
        return nx.adjacency_matrix(G).todense()
    
    '''
    Método para obtener un diccionario de personajes haciendo web scraping
    '''
    def scrapeWiki(self,url):
        web = urllib.request.urlopen(url)
        html = BeautifulSoup(web.read(), "html.parser")
        for pers in html.find_all("a", {"class": "category-page__member-link"}):
            pn = pers.get('title')
            self.anadirPersonaje(pn)
        
    '''
    Método para importar un diccionario de personajes desde un fichero csv
    '''
    def importDict(self, fichero):
        self.__csv.importDict(fichero)
    
    '''
    Método para exportar el diccionario de personajes a un fichero csv
    '''
    def exportDict(self, fichero):
        self.__csv.exportDict(fichero)
         
    '''
    Método para obtener el texto del epub del que se quiere obtener la red de 
    personajes
    '''
    def obtTextoEpub(self,fichero):
        l = lecturaEpub.lecturaEpub(fichero)
        self.__texto = ''
        for f in l.siguienteArchivo():
            self.__texto += f

    def getTexto(self):
        return self.__texto