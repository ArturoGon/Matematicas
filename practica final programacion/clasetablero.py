# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:37:39 2016

@author: Teresa
"""
from clasefichas import Fichas


class Tablero:
    
    def __init__(self):
        
        self.__matriz=[]
        for i in range(16):
            fila =[' '] *15
            self.__matriz.append(fila)
        
    
    def imprimir(self):
        i=1
        print "    " + str(0),
        while (i <= 10):
            print "   " + str(i) , 
            i=i+1
        while (i <= 14):
             print "  " + str(i) , 
             i=i+1
        print ""    
        for i in range(0, len(self.__matriz)-1):
            if ((0+i)<=9):
                print str(0+i) + ' | ',
            else:
                print str(0+i) + '| ',
            for j in range(0, len(self.__matriz)-1):
                print self.__matriz[i][j] + ' | ',
            print ""
                
    
    def colocar(self, palabra, fichas, x, y, direccion):
        
        if (direccion =='H'):
            for i in range(0,(palabra.longitud())):
                w= palabra.getLetra(i)
                if(self.__matriz[y][x+i] != w):
                    self.__matriz[y][x+i]= w
                    fichas.eliminar(w)
                
        else:
            for i in range(0,(palabra.longitud())):
                w= palabra.getLetra(i)
                if(self.__matriz[y+i][x] != w):
                    self.__matriz[y+i][x]= w
                    fichas.eliminar(w)
                

    def esPosible(self, palabra, x, y, direccion, palabrascolocadas):
       
        # si se sale de los limites
        if (x>14) or (y>14) or (x<0) or (y<0):  
            return False
            
        elif (palabra.longitud()>(14-x)) and (direccion =='H'):
            return False
            
        elif (palabra.longitud()>(14-y)) and (direccion=='V'):
            return False 
        
        #si es la primera palabra y no pasa por el centro
        elif (palabrascolocadas==0):
            if (x!=7) or (y!=7):
                return False
            
        #ya hay otra ficha puesta
        elif (direccion=='H'):
            for e in range (0, palabra.longitud()):
                w=palabra.getLetra(e)
                if (self.__matriz[y][x+e]!=' ') and (self.__matriz[y][x+e] != w):
                    return False 
                    
        elif (direccion =='V'):
            for e in range (0, palabra.longitud()):
                w=palabra.getLetra(e)
                if (self.__matriz[y+e][x]!=' ') and (self.__matriz[y+e][x]!= w):
                    return False
                
        #no utiliza una ficha ya colocada si hay una o mas palabras colocadas
        if(palabrascolocadas!=0) and (direccion =='H'):
            iguales=0
            for i in range(0,palabra.longitud()):
                w= palabra.getLetra(i)
                if(self.__matriz[y][x+i] == w):
                    iguales = iguales +1
            if (iguales == 0):
                return False
                   
        elif(palabrascolocadas!=0) and (direccion =='V'):
            iguales=0
            for i in range(0, palabra.longitud()):
                w= palabra.getLetra(i)
                if(self.__matriz[y+i][x] == w):
                    iguales = iguales +1
            if (iguales == 0):
                return False
    
        #antes de la palabra o al final hay una ficha
        if (palabrascolocadas!=0) and (direccion =='H'):
            q = palabra.longitud()
            if (self.__matriz[y][x-1] !=' ') or (self.__matriz[y][x+q]!=' '):
                return False
                
        elif (palabrascolocadas!=0) and (direccion =='V'):
            q = palabra.longitud()
            if (self.__matriz[y-1][x]!=' ') or (self.__matriz[y+q][x]!=' '):
                return False
        
        #no coloca ficha
        if (palabrascolocadas!=0) and (direccion =='H'):
            fichasiguales=0
            for i in range(0,palabra.longitud()):
                w= palabra.getLetra(i)
                if(self.__matriz[y][x+i] == w):
                    fichasiguales = fichasiguales +1
            if (fichasiguales==(palabra.longitud())):
                return False
            
        elif (palabrascolocadas!=0) and (direccion =='V'):
            fichasiguales=0
            for i in range(0,palabra.longitud()):
                w= palabra.getLetra(i)
                if(self.__matriz[y+i][x] == w):
                    fichasiguales = fichasiguales +1
            if (fichasiguales == (palabra.longitud())):
                return False
                
        #si es posible colocarla
        return True
        
   
    def getFichas(self, palabra, x, y, direccion):
        
        fichasnecesarias = Fichas()
        
        if (direccion =='H'):
            for n in range(0, palabra.longitud()):
                w= palabra.getLetra(n)
                if(self.__matriz[y][x+n] != w):
                    fichasnecesarias.addFichas(w,1)
        
        else:
            for n in range(0, palabra.longitud()):
                w= palabra.getLetra(n)
                if(self.__matriz[y+n][x] != w):
                    fichasnecesarias.addFichas(w,1)
        
        return fichasnecesarias
    
    #nofunciona
    def mostrarcolocacion(self, palabra, palabrascolocadas):
        
        direc=["H","V"]
        for x in range (0,len(self.__matriz)):
            for y in range (0,len(self.__matriz)):
                for d in direc:
                    if (self.esPosible(palabra,x,y,d,palabrascolocadas)):
                        print ' ',x,y,d
        
#==============================================================================
#         direc='H'
#         for x in range (0,len(self.__matriz)):
#             for y in range (0,len(self.__matriz)):
#                 if (self.esPosible(palabra,x,y,direc,palabrascolocadas)) and (direccion.getLetra(0)=='H'):
#                     print ' ',x,y,direc
#          
#         direc='V'
#         for x in range (0,len(self.__matriz)):
#             for y in range (0,len(self.__matriz)):
#                 if (self.esPosible(palabra,x,y,direc,palabrascolocadas)) and (direccion.getLetra(0)=='H'):
#                     print ' ',x,y,direc
#==============================================================================
        