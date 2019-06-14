# -*- coding: utf-8 -*-

class TempBD:
    
    __instance = None
    
    def __init__(self):
        if TempBD.__instance is not None:
            raise Exception("An instance already exists!")
        self.__sesiones = dict()
        self.__nextID = 0
        if(TempBD.__instance == None):
            TempBD.__instance = self
            
    @staticmethod
    def getInstance():
        if(TempBD.__instance == None):
            TempBD()
        return TempBD.__instance
    
    def addSesion(self, sesionObject):
        self.__nextID += 1
        self.__sesiones[self.__nextID] = sesionObject
        return self.__nextID
    
    def delSesion(self, sesionID):
        del self.__sesiones[sesionID]
        
    def replaceObject(self, sesionID, sesionObject):
        self.__sesiones[sesionID] = sesionObject
        
    def getObject(self, sesionID):
        return self.__sesiones[sesionID]
    
    def getSesiones(self):
        return self.__sesiones