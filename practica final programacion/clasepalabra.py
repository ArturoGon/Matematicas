# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:03:56 2016

@author: Teresa
"""

import sys

from clasetablafrecuencias import TablaFrecuencias


class Palabra:
    
    __letra = ' '
    __letra_f = ' '
    
    
    def __init__(self):
        self.__palabra =  []
       
 
    @staticmethod
    def saltar_blancos():
        while ((Palabra.__letra == ' ') or (Palabra.__letra == '\n')):
            Palabra.__letra = sys.stdin.read(1)
    
                
    @staticmethod    
    def leer_palabra():
        p = Palabra()
        Palabra.saltar_blancos()
        while ((Palabra.__letra!=' ') and (Palabra.__letra!='\n')):
            p.__palabra.append(Palabra.__letra)
            Palabra.__letra = sys.stdin.read(1)
       
        return p
        
        
    def mostrarPalabra(self):
        longitudpalabra= len(self.__palabra)
        for i in range (0, longitudpalabra):
            sys.stdout.write(self.__palabra[i])
        print " "
    
        
    def esVacia(self):
        return len(self.__palabra) == 0


    def __str__(self):
        cadena = ""
        longitudpalabra= len(self.__palabra)
        for i in range (0, longitudpalabra):
            cadena +=(self.__palabra[i])
        
        return cadena
        
        
    def esIgual_a(self, p2):
        if (len(self.__palabra) != len(p2.__palabra)):
            return False
        i= 0        
        while ((i< len(self.__palabra)-1)) and (self.__palabra[i] == p2.__palabra[i]):
            i= i + 1
        if(i==len(self.__palabra)-1):
            return True
        else:
            return False
       
            
    @staticmethod    
    def leer_Fichero(fichero):
        p = Palabra()
        Palabra.__letra_f = ' '
        Palabra.saltar_blancosFichero(fichero)
        while ((Palabra.__letra_f!=' ') and (Palabra.__letra_f!='\n') and (Palabra.__letra_f!="")):
            p.__palabra.append(Palabra.__letra_f)
            Palabra.__letra_f = fichero.read(1)
       
        return p
        
        
    @staticmethod
    def saltar_blancosFichero(fichero):
        while ((Palabra.__letra_f == ' ') or (Palabra.__letra_f == '\n') ):
            Palabra.__letra_f = fichero.read(1)
    
            
    def getFrecuencias(self):
      tf= TablaFrecuencias()
      
      for palabra in self.__palabra:
          tf.actualizar(palabra)
          
      return tf


    def getLetra(self,i):
        return self.__palabra[i]
        
    
    def longitud(self):
        return len(self.__palabra)   

        
    def a_entero_palabras(self):
       num=0
       for i in range (0, len(self.__palabra)):
            num= (num*10) + int (self.__palabra[i])
       
       return num
        
        