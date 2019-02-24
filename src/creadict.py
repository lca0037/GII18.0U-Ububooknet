# -*- coding: utf-8 -*-
import ply.lex as lex
from src import personaje as p

class creadict:
    
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.aux = dict()
        
    tokens = ("PERSONAJE", "ESPACIOS", "PUNTO", "CARACTER", "OTRO")
    states = (('punto','exclusive'),)
    
    
    def t_PERSONAJE(self,t): 
        r"[A-Z\300-\335][a-z\340-\377]+(\s[A-Z\300-\335]([a-z\340-\377]+|\.))*"
        return t
    
    def t_ESPACIOS(self,t):
        r"[\s]"
    
    def t_PUNTO(self,t):
        r"\.[\s]"
        t.lexer.begin('punto')
        
    def t_CARACTER(self,t):
        r"."
    
    def t_punto_PERSONAJE(self,t):
        r"[A-Z\300-\335][a-z\340-\377]+(\s[A-Z\300-\335]([a-z\340-\377]+|\.))+"
        t.lexer.begin('INITIAL')
        return t
    
    def t_punto_OTRO(self,t):
        r"[^\s\.]+"
        t.lexer.begin('INITIAL')
    
    def t_punto_error(self,t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
    def t_error(self,t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def crearDict(self, texto):
        txt = ". " + texto
        lex.input(txt)
        personajes = dict()
        numpers = 0
        for tok in iter(lex.token, None):
            if(tok.value in self.aux.keys()):
                self.aux[tok.value]+=1
            else:
                self.aux[tok.value]=1
        
        for k in self.aux.keys():
            personajes[numpers]= p.personaje(k,self.aux[k])
            numpers+=1
        
        return personajes, numpers