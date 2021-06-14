# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:02:42 2016

@author: Teresa
"""

import random

from clasetablafrecuencias import TablaFrecuencias

class Fichas:
#constructor del array
  def __init__(self):
    self.__fichas=[]

      
  def addFichas(self,c,n):
     for i in range (0,n):
         self.__fichas.append(c)
         
#guarda todas las fichas en el array        
  def CrearBolsa(self):
      self.addFichas("A",12)
      self.addFichas("B",2)
      self.addFichas("C",4)
      self.addFichas("D",5)
      self.addFichas("E",12)
      self.addFichas("F",1)
      self.addFichas("G",2)
      self.addFichas("H",2)
      self.addFichas("I",6)
      self.addFichas("J",1)
      self.addFichas("L",4)
      self.addFichas("M",2)
      self.addFichas("N",5)
      self.addFichas("O",9)
      self.addFichas("P",2)
      self.addFichas("Q",1)
      self.addFichas("R",5)
      self.addFichas("S",6)
      self.addFichas("T",4)
      self.addFichas("U",5)
      self.addFichas("V",1)
      self.addFichas("W",1)
      self.addFichas("X",1)
      self.addFichas("Y",1)
      self.addFichas("Z",1)
      
#enseña las fichas que se encuentran en el array         
  def __str__(self):
      
      return str(self.__fichas)
      
#saca de forma aleatoria las fichas de la bolsa para el jugador   
  def sacarFicha(self):
        numFichas= len(self.__fichas)-1
        n= random.randrange(0, (numFichas), 1)
      
        return  self.__fichas.pop(n)
        
 
  def eliminar(self, ficha):
        
        return  self.__fichas.remove(ficha)
      
        
  def getFrecuencias(self):
      tf=TablaFrecuencias()
     
      for ficha in self.__fichas:
          tf.actualizar(ficha)
      
      return tf
      
      
  def a_entero_fichas(self):
       num=0
       for i in range (0 , len(self.__fichas)):
            num= (num*10) + int (self.__fichas[i])
        
       return num
  
       
  @staticmethod     
  def darfichas(e , fichas_jugador,fichas):
      fichas.longitud()
      if((fichas.longitud())>=(7-(fichas_jugador.longitud()))):
          for i in range (e,7):
              f = fichas.sacarFicha()
              fichas_jugador.addFichas(f,1)
      else :
          for i in range (0, (len(fichas)+1)):
              f = fichas.sacarFicha()
              fichas_jugador.addFichas(f,1)
              
      return fichas_jugador
  
      
  def longitud(self):
        return len(self.__fichas) 