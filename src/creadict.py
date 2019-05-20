# -*- coding: utf-8 -*-
import ply.lex as lex

'''
Clase que crea un diccionario de manera automática

@author: Luis Miguel Cabrejas
'''
class creadict:
    
    '''
    Constructor de la clase
    '''
    def __init__(self, modusuario):
        self.lexer = lex.lex(module=self)
        self.aux = dict()
        self.mod = modusuario
      
    #Tokens del lexer
    tokens = ("PERSONAJE", "ESPACIOS", "PUNTO", "CARACTER", "OTRO")
    #Estados del lexer
    states = (('punto','exclusive'),)
    
    
    '''
    Función del lexer que comprueba si hay una palabra en mayúsculas
    '''
    def t_PERSONAJE(self,t): 
        r"[A-Z\300-\335][a-z\340-\377]+((\s|\-)?[A-Z\300-\335]([a-z\340-\377]+|\.))*"
        return t
    
    '''
    Comprueba si hay un espacio
    '''
    def t_ESPACIOS(self,t):
        r"[\s]"
    
    '''
    Función del lexer que comprueba si hay un signo que indica que la siguiente
    palabra pueda estar en mayúsculas sin llegar a ser un nombre propio y 
    cambia de estado para comprobarlo
    '''
    def t_PUNTO(self,t):
        r"(\.+)|[\(\)\[\]<>\'\":;¿\?¡!=\-_\253\273—]"
        t.lexer.begin('punto')
        
    '''
    Función del lexer
    '''
    def t_CARACTER(self,t):
        r"."
    
    '''
    Función del lexer para salir del estado punto si no hay un personaje
    '''
    def t_punto_OTRO(self,t):
        r"[^\s\.\(\)\[\]<>\'\":;¿\?¡!=\-_\253\273—]+"
        t.lexer.begin('INITIAL')
        
    def t_punto_ESPACIOS(self,t):
        r"[\s\.\(\)\[\]<>\'\":;¿\?¡!=\-_\253\273—]"
    
    def t_punto_error(self,t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
    def t_error(self,t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    '''
    Función que comienza el recorrido del texto para obtener un diccionario de
    personajes
    '''
    def crearDict(self, texto):
        txt = ". " + texto
        lex.input(txt)
        for tok in iter(lex.token, None):
            if(tok.value not in self.aux.keys()):
                self.aux[tok.value] = None
                self.mod.anadirPersonaje(tok.value, tok.value)
    