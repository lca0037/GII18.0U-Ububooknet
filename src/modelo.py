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
import json
from bs4 import BeautifulSoup
import zipfile

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
        self.__fichero = None
        self.__csv = lectorcsv.lectorcsv(self)
        self.__idioma = None
        self.__configVis = {'Path to file (csv or json)': 'https://gist.githubusercontent.com/ulfaslak/6be66de1ac3288d5c1d9452570cbba5a/raw/0b9595c09b9f70a77ee05ca16d5a8b42a9130c9e/miserables.json', 'Apply heat (wiggle)': False, 'Charge strength': -50, 'Center gravity': 0.1, 'Link distance': 10, 'Link width': 5, 'Link alpha': 0.5, 'Node size': 10, 'Node stroke size': 0.5, 'Node size exponent': 0.5, 'Link width exponent': 0.5, 'Collision': False, 'Node fill': '#16a085', 'Node stroke': '#000000', 'Link stroke': '#7c7c7c', 'Label stroke': '#000000', 'Show labels': True, 'Show singleton nodes': False, 'Node size by strength': True, 'Zoom': 1.5, 'Min. link weight %': 0, 'Max. link weight %': 100}
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
        l = lecturaEpub.lecturaEpub(self.__fichero)
        posper = pp.pospersonajes()
        cap = ''
        pers = self.getDictParsear()
        self.__fincaps = list() 
        posiciones = list()
        for f in l.siguienteArchivo():
            cap = ". " + f
            pos,fin = posper.obtenerPos(cap, pers)
            posiciones.append(pos)
            self.__fincaps.append(fin)
        for i in self.personajes.keys():
            self.personajes[i].lennombres = dict()
            pers = self.personajes[i].getPersonaje()
            for n in pers.keys():
                c = 1
                apar = 0
                for posc in posiciones:
                    if(n in posc.keys()):
                        pers[n][c] = posc[n]
                        apar+=len(posc[n])
                    c+=1
                self.personajes[i].lennombres[n]=apar
                self.personajes[i].sumNumApariciones(apar)
      
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
            y.append(self.personajes[k].getNumApariciones()[0])
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
    def anadirPersonaje(self, idpers, pers):
        if(idpers not in self.personajes):
            self.personajes[idpers] = p.personaje()
            self.personajes[idpers].getPersonaje()[pers] = dict()
            self.numpers+=1
            return 'Personaje añadido correctamente'
        return 'La id de personaje ya existe'
    '''
    Método para eliminar personajes
    '''
    def __eliminarPersonaje(self, idPersonaje):
        if(idPersonaje in self.personajes):
            del self.personajes[idPersonaje]
       
    '''
    Método para eliminar una lista de personajes
    '''
    def eliminarListPersonajes(self, personajes):
        for idp in personajes:
            self.__eliminarPersonaje(idp)
    
    '''
    Método para juntar personajes
    '''
    def __juntarPersonajes(self, idPersonaje1, idPersonaje2):
        if(idPersonaje1 in self.personajes and idPersonaje2 in self.personajes):
            pers1 = self.personajes[idPersonaje1].getPersonaje()
            pers2 = self.personajes[idPersonaje2].getPersonaje()
            apar1 = self.personajes[idPersonaje1].lennombres
            apar2 = self.personajes[idPersonaje2].lennombres
            for k in pers2.keys():
                if k not in pers1.keys():
                    pers1[k]=pers2[k]
                    if(k in apar2.keys()):
                        apar1[k] = apar2[k]
                        self.personajes[idPersonaje1].sumNumApariciones(apar2[k])
            self.__eliminarPersonaje(idPersonaje2)
    
    '''
    Método para juntar una lista de personajes en uno solo
    '''
    def juntarListPersonajes(self,lista):
        for i in range(1,len(lista)):
            self.__juntarPersonajes(lista[0],lista[i])
    
    '''
    Método para añadir otro nombre para referirse a un personaje
    '''
    def anadirReferenciaPersonaje(self,idp,ref):
        self.personajes[idp].getPersonaje()[ref]= dict()
    
    '''
    Método que elimina una referencia a un personaje
    '''
    def __eliminarReferenciaPersonaje(self,idp,ref):
        if(idp in self.personajes.keys()):
            p = self.personajes[idp].getPersonaje()
            if(ref in p.keys()):
                if (len(p)>1):
                    del p[ref]
                    if(ref in self.personajes[idp].lennombres):
                        self.personajes[idp].resNumApariciones(self.personajes[idp].lennombres[ref])
                        del self.personajes[idp].lennombres[ref]
                else:
                    del self.personajes[idp]
    
    '''
    Método para eliminar una lista de referencias de sus respectivos personajes
    '''
    def eliminarListRefs(self,lista):
        for l in lista:
            self.__eliminarReferenciaPersonaje(l[0],l[1])
            
    '''
    Método para modificar los id de los personajes
    '''
    def modificarIdPersonaje(self,idact,newid):
        self.personajes[newid] = self.personajes.pop(idact)
    
    '''
    Método que junta las posiciones de todos los nombres de un personaje
    '''
    def juntarPosiciones(self):
        for i in self.personajes.keys():
            pers = self.personajes[i].getPersonaje()
            pos = {}
            for n in pers.keys():
                    for caps in pers[n].keys():
                        cont = 0
                        if(caps not in pos.keys()):
                            pos[caps]=list()
                        for j in pers[n][caps]:
                            while(cont<len(pos[caps]) and pos[caps][cont]<j):
                                cont+=1
                            pos[caps].insert(cont,j)
            self.personajes[i].setPosicionPers(pos)
       
    def prepararRed(self):
        self.obtenerPosPers()
        self.juntarPosiciones()
    '''
    Método para obtener una matriz de adyacencia de las relaciones entre los personajes
    '''
    def getMatrizAdyacencia(self):
        return nx.adjacency_matrix(self.__G).todense()
    
    '''
    Método para generar un grafo a partir de las relaciones de los personajes
    '''
    def generarGrafo(self,rango,minapar,caps):
        persk = list(self.personajes.keys())
        tam = len(persk)
        self.__G = nx.Graph()
        for i in range(tam):
            #Se comprueba que se cumple con el requisito mínimo de apariciones
            if(self.personajes[persk[i]].getNumApariciones()[0]>=minapar):
                #La red es no dirigida sin autoenlaces así que no hace falta medir el peso 2 veces ni consigo mismo
                for j in range(i+1,tam):
                    #Se comprueba que cumple el requisito mínimo de apariciones
                    if(self.personajes[persk[j]].getNumApariciones()[0]>=minapar):
                        peso=0
                        #Se recorren los capítulos
                        for cap in self.personajes[persk[i]].getPosicionPers().keys():
                            #Se obtienene las posiciones del personaje en el capítulo correspondiente
                            for posi in self.personajes[persk[i]].getPosicionPers()[cap]:
                                prev = False
                                post = False
                                #Si no se tienen en cuenta los capítulos
                                if(not caps):
                                    aux = posi-rango
                                    capaux = cap
                                    #Si aux negativo se ha pasado al capítulo anterior capaux minimo de 2 para no salirnos de la lista
                                    while(aux<0 and capaux>1):
                                        prev = True
                                        capaux-=1
                                        aux = self.__fincaps[capaux-1] + aux
                                        #Si aux menor que 0 nos hemos saltado más de un capítulo
                                        if(aux<0):
                                            #Como nos hemos saltado el capítulo entero consideramos todas las posiciones que tiene el 
                                            #segundo personaje en ese capítulo como relación
                                            peso+=len(self.personajes[persk[j]].getPosicionPers()[capaux])
                                        else:
                                            #Comprobamos todas las palabras del capítulo previo que no nos hemos saltado por completo y añadimos
                                            #las que se encuentren en el rango
                                            for posj in self.personajes[persk[j]].getPosicionPers()[capaux]:
                                                if(posj>=aux):
                                                    peso+=1
                                    #Se repite el proceso anterior pero para capítulos posteriores
                                    aux = posi + rango - self.__fincaps[cap-1]
                                    capaux = cap
                                    while(aux>0 and capaux<len(self.__fincaps)):
                                        capaux+=1
                                        post=True
                                        if(aux>self.__fincaps[capaux-1]):
                                            aux = aux - self.__fincaps[capaux-1]
                                            peso+=len(self.personajes[persk[j]].getPosicionPers()[capaux])
                                        else:
                                            for posj in self.personajes[persk[j]].getPosicionPers()[capaux]:
                                                if(posj<=aux):
                                                    peso+=1
                                                else:
                                                    break
                                #Si se ha pasado al capítulo previo y al posterior se añaden directamente todas las posiciones del actual
                                if(not caps and prev and post):
                                    peso+=len(self.personajes[persk[j]].getPosicionPers()[cap])
                                else:
                                    #Se comprueba en el capítulo actual las palabras que entran en el rango
                                    for posj in self.personajes[persk[j]].getPosicionPers()[cap]:
                                        if(posj>=(posi-rango)):
                                            if(posj<=(posi+rango)):
                                                peso+=1
                                            else:
                                                break
                        if(peso>0):
                            self.__G.add_edge(persk[i],persk[j],weight=peso)
    
    '''
    Método para mandar a d3 la información para visualizar la red
    '''
    def visualizar(self):
        return json.dumps(nx.json_graph.node_link_data(self.__G))
        
    '''
    Método para obtener un diccionario de personajes haciendo web scraping
    '''
    def scrapeWiki(self,url):
        web = urllib.request.urlopen(url)
        html = BeautifulSoup(web.read(), "html.parser")
        for pers in html.find_all("a", {"class": "category-page__member-link"}):
            pn = pers.get('title')
            self.anadirPersonaje(pn,pn)
        
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
    def obtTextoEpub(self):
        l = lecturaEpub.lecturaEpub(self.__fichero)
        self.__texto = ''
        for f in l.siguienteArchivo():
            self.__texto += ". " + f

    '''
    Obtiene el texto del epub
    '''
    def getTexto(self):
        return self.__texto
        
    '''
    Método para comprobar si un archivo es un epub
    '''
    def esEpub(self,fich):
        if(not zipfile.is_zipfile(fich)):
            return False
        x = zipfile.ZipFile(fich)
        try:
            x.read('META-INF/container.xml')
        except:
            return False
        else:
            return True
    '''
    Establece el epub a leer
    '''
    def setFichero(self, fich):
        self.__fichero = fich
        
    '''
    Devuelve si hay un fichero o no
    '''
    def hayFichero(self):
        if(self.__fichero != None):
            return True
        return False
    
    '''
    Método que devuelve la configuración de la visualización
    '''
    def getConfigVis(self):
        return self.__configVis
    
    '''
    Método que guarda la configuración de la visualización
    '''
    def setConfigVis(self,newconfig):
        self.__configVis = newconfig
        
    def setIdioma(self,lang):
        self.__idioma = lang
        
    def getIdioma(self):
        return self.__idioma
    
    def exportGML(self,filename):
        self.writeFile(filename,nx.generate_gml(self.__G))
        
    def exportGEXF(self,filename):
        self.writeFile(filename,nx.generate_gexf(self.__G))
    
    def exportPajek(self,filename):
        nx.write_pajek(self.__G, filename)
        
    def writeFile(self,filename,text):
        file = open(filename,"w")
        for r in text:
            file.write(r)
        