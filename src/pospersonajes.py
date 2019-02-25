# -*- coding: utf-8 -*-
import ply.lex as lex

class pospersonajes:
    
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.nombres = list()
        self.nomscoinc = list()
        self.contador = 1
        self.aux = list()
        self.cadaux = ""
        self.ultcoinc = ""
        self.resul = dict()
    
    tokens = ("PALABRA", "ESPACIO")
    states = (('coincidencia','exclusive'),)
    
    def t_PALABRA(self, t):
        r"[^\s.,()\[\]<>\'\":;¿?¡!=\-_]+"
        self.nomscoinc = self.esSubcadena(t.value, self.nombres)
        ncoinc = len(self.nomscoinc)
        if(ncoinc > 0):
#            print('Cadena:', self.esSubcadena(t.value, self.nombres))
            if(ncoinc == 1 and t.value in self.nomscoinc):
#                print('Coincidencia única:',t.value,'. Número de palabra:',self.contador)
                self.resul[t.value].append(self.contador)
                self.contador += 1
            else:
                self.ultcoinc = ""
                self.aux = list()
                if(t.value in self.nomscoinc):
                    self.ultcoinc = t.value
                else:
                    self.aux.append(t.value)
                self.cadaux = t.value
#                print('Cambio a estado coincidencia con:',self.cadaux)
                t.lexer.begin('coincidencia')
        else:
#            print('Sin coincidencias:',t.value,'. Número de palabra:',self.contador)
            self.contador += 1
        
    def t_ESPACIO(self, t):
        r"[\s.,()\[\]<>\'\":;¿?¡!=\-_]+"
        
    def t_coincidencia_PALABRA(self, t):
        r"([^\s.,()\[\]<>\'\":;¿?¡!=\-_]+|[\s.,()\[\]<>\'\":;¿?¡!=\-_])"
        self.cadaux += t.value
#        print('Coinc previas:',self.nomscoinc)
        self.nomscoinc = self.esSubcadena(self.cadaux, self.nomscoinc)
#        print('Coinc actuales:',self.nomscoinc)
        ncoinc = len(self.nomscoinc)
        if(ncoinc > 0):
            if(ncoinc == 1 and self.cadaux in self.nomscoinc):
#                print('Coincidencia única en estado coincidencia:',self.cadaux,'. Número de palabra:',self.contador)
                t.lexer.begin('INITIAL')
                self.resul[self.cadaux].append(self.contador)
                self.aux = list()
                self.contador += 1
            else:
#                print('Mult coinc o coinc no completa:',self.cadaux)
                if(self.cadaux in self.nomscoinc):
                    self.ultcoinc = self.cadaux
                    self.aux = list()
                else:
                    self.aux.append(t.value)
#                print('Última coincidencia:',self.ultcoinc,'lista auxiliar:',self.aux)
        else:
            self.aux.append(t.value)
#            print('Sin coincs en estado coincidencias, última coinc:',self.ultcoinc,'palabra actual:',self.contador,'cadena actual:',self.cadaux,'lista aux:',self.aux)
            t.lexer.begin('INITIAL')
            self.resul[self.ultcoinc].append(self.contador)
            self.contador += 1
            txt = ""
            for i in self.aux:
                txt += i
            clon = self.lexer.clone()
            clon.input(txt)
            for tok in iter(clon.token, None):
                print()
        
    def t_error(self, t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
    def t_coincidencia_error(self, t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
    def obtenerPos(self, texto, nombres):
        self.nombres = nombres
        for n in nombres:
            self.resul[n] = list()
        lex.input(texto)
        for tok in iter(lex.token, None):
            print()
        return self.resul
                
    def esSubcadena(self,st,lista):
        l = list()
        aux = True
        for pal in lista:
            if(len(pal)>=len(st)):
                for i in range(len(st)):
                    if(st[i] != pal[i]):
                        aux = False
                        break
            else:
                aux = False
            if(aux):
                l.append(pal)
            else:
                aux = True
        return l
