# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:01:36 2016

@author: Teresa
"""



from clasepalabra import Palabra
from clasetablafrecuencias import TablaFrecuencias
class Diccionario:
    
    def __init__(self,nombre):
        
        self.__nombre = nombre
    
        
    def comprobarPalabra(self,p):
        
        fichero = open (self.__nombre,"r") 
        w = Palabra.leer_Fichero(fichero)
        
        while (not p.esIgual_a(w) ) and (not w.esVacia()):
            w = Palabra.leer_Fichero(fichero)
        fichero.close()
        
        if (p.esIgual_a(w)):
            return True
        else:
            return False
            
    def mostrarPalabra(self, f):
        fichero = open (self.__nombre,"r") 
        w = Palabra.leer_Fichero(fichero)
        tf_w= w.getFrecuencias()
        
        while (not w.esVacia()):
            if (TablaFrecuencias.esSubconjunto(f, tf_w)):
                print w
            w = Palabra.leer_Fichero(fichero)
            tf_w= w.getFrecuencias()
            
        fichero.close()
        
        
        