# -*- coding: utf-8 -*-
"""
Clase con la que la vista interactua

@author: luism
"""

import ply.lex as lex
import personaje as p
import matplotlib.pyplot as plt
import numpy as np

class modelo:
    
    def __init__(self):
        self.texto = 'Esto es un documento de pruebas para comprobar que se obtienen'
        self.texto += ' bien las palabras en mayúsculas. Felipe, esto es texto de '
        self.texto += 'relleno Pedro Pérez, Josema esto es más texto de relleno para'
        self.texto += ' poder hacer pruebas Pedro esto sigue siendo relleno Pedro '
        self.texto += 'Rodríguez, Pedro, texto de relleno. María se fue a poner más '
        self.texto += 'texto de relleno. Pedro Pérez esto como no sigue siendo texto'
        self.texto += ' de pruebas Ana.'
        self.personajes= dict()
        self.numpers = 0
        self.sigid = 0
     
    def crearDiccionario(self):
        tokens = ("PERSONAJE", "ESPACIOS", "PUNTO", "CARACTER", "OTRO")
        states = (('punto','exclusive'),)
        aux = dict()
        
        def t_PERSONAJE(t): 
            r"[A-Z\300-\335][a-z\340-\377]+(\s[A-Z\300-\335]([a-z\340-\377]+|\.))*"
            return t
        
        def t_ESPACIOS(t):
            r"[\s]"
        
        def t_PUNTO(t):
            r"\.[\s]"
            t.lexer.begin('punto')
            
        def t_CARACTER(t):
            r"."
        
        def t_punto_PERSONAJE(t):
            r"[A-Z\300-\335][a-z\340-\377]+(\s[A-Z\300-\335]([a-z\340-\377]+|\.))+"
            t.lexer.begin('INITIAL')
            return t
        
        def t_punto_OTRO(t):
            r"[^\s\.]+"
            t.lexer.begin('INITIAL')
        
        def t_punto_error(t):
            print ("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)
            
        def t_error(t):
            print ("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)
    
        lex.lex()
        txt = ". " + self.texto
        lex.input(txt)
        for tok in iter(lex.token, None):
            if(tok.value in aux.keys()):
                aux[tok.value]+=1
            else:
                aux[tok.value]=1
                self.numpers+=1
        
        for k in aux.keys():
            self.personajes[self.sigid]= p.personaje(k,aux[k])
            self.sigid+=1
            
    def getPersonajes(self):
        return self.personajes
    
    def histogramaPersonajes(self):
        x = list()
        y = list()
        for k in self.personajes.keys():
            p = self.personajes[k].getPersonaje()
            for sk in p.keys():
                x.append(sk)
                y.append(p[sk])
        tam = np.arange(self.numpers)
        plt.title('Frecuencia personajes')
        plt.xlabel('Nombre')
        plt.ylabel('Apariciones')
        plt.bar(tam,height=y)
        plt.xticks(tam,x)
    
    def anadirPersonaje(self, pers):
        self.personajes[self.numpers] = p.personaje(pers,0)
        self.numpers+=1
        
    def eliminarPersonaje(self, idPersonaje):
        if(idPersonaje in self.personajes):
            del self.personajes[idPersonaje]
        
    def juntarPersonajes(self, idPersonaje1, idPersonaje2):
        if(idPersonaje1 in self.personajes and idPersonaje2 in self.personajes):
            pers1 = self.personajes[idPersonaje1].getPersonaje()
            pers2 = self.personajes[idPersonaje2].getPersonaje()
            for k in pers2.keys():
                if k in pers1.keys():
                    pers1[k]+=pers2[k]
                else:
                    pers1[k]=pers2[k]
            self.eliminarPersonaje(idPersonaje2)
    
#m = modelo()
#m.crearDiccionario()
#m.histogramaPersonajes()
#m.anadirPersonaje('Andrea')
#m.histogramaPersonajes()
#m.anadirPersonaje('Paola')
#m.histogramaPersonajes()