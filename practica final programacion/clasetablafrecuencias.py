# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:04:11 2016

@author: Teresa
"""



class TablaFrecuencias:
    
    def __init__(self):
        # creacion del array mediante funcion de generacion
        self.letras = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        self.frecuencias = [0 for x in range(0, len(self.letras))]
        self.otros = 0

        
    def actualizar(self, c):    
        i = 0
        while ((i < len(self.letras)-1) and (c != self.letras[i])):
            i = i + 1
    
        if (c == self.letras[i]):
            self.frecuencias[i] = self.frecuencias[i] + 1
        else:
            self.otros = self.otros + 1

            
    def mostrar(self):
        for i in range(0, len(self.letras)):
            if (self.frecuencias[i] != 0):
                print "Letra '" + self.letras[i] + "' aparece " + str(self.frecuencias[i]) + " veces."
        print "Otros " + str(self.otros)
        
        
    @staticmethod
    def esSubconjunto(fichas, palabra):
       i=0
       while (i <= len(fichas.frecuencias)-1) and (palabra.frecuencias[i]<= fichas.frecuencias[i] ) :
           
           i = i + 1 
           #print fichas.frecuencias[i], palabra.frecuencias[i], i
    
       return i == (len(fichas.frecuencias))