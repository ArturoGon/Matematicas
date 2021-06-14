# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:04:59 2016

@author: Teresa
"""
from clasefichas import Fichas
from clasepalabra import Palabra
from clasediccionario import Diccionario
from clasetablafrecuencias import TablaFrecuencias
from clasetablero  import Tablero 

fichas=Fichas()
fichas_jugador = Fichas()
diccionario= Diccionario("diccionario.txt")
tf=TablaFrecuencias()
tablero=Tablero()

print "                             JUEGO APALABRADOS"
print " "
#crea todas las fichas y las enseña
fichas.CrearBolsa()
#muestra el tablero
tablero.imprimir()
print " "
#saca las 7 fichas para jugar y enseña las que quedan
for i in range (1,8):
    f = fichas.sacarFicha()
    fichas_jugador.addFichas(f,1)

tf_fichas_jugador= fichas_jugador.getFrecuencias()
    
print "Tus fichas para jugar son: " + str(fichas_jugador)
print " "

palabrascolocadas=0 
fichascolocadas=0

print ""
print "Dime la palabra que quieres colocar (Escriba AYUDAPALABRA para mostrarle las opciones):"
primera = Palabra.leer_palabra()
if (str(primera)== "AYUDAPALABRA" ):
         diccionario.mostrarPalabra(tf_fichas_jugador)
         print "Dime la palabra que quieres colocar:"
         primera = Palabra.leer_palabra()
    
while (str(primera) != "EXIT"):
    
    tf_primera= primera.getFrecuencias()
    print " "
    
    print "Dime las coordenadas:"
    print "x:"
    x= Palabra.leer_palabra()
    x=x.a_entero_palabras()
    
    print "y:"
    y=Palabra.leer_palabra()
    y = y.a_entero_palabras()
    
    print "Dime la direccion(H o V):"
    p_direccion=Palabra.leer_palabra()
    direccion = p_direccion.__str__()

    fichasnecesarias = tablero.getFichas(primera, x, y, direccion)
    
    if (tablero.esPosible(primera, x, y, direccion, palabrascolocadas)) and (TablaFrecuencias.esSubconjunto(tf_fichas_jugador, fichasnecesarias.getFrecuencias())) and (diccionario.comprobarPalabra(primera)):
        
        tablero.colocar( primera , fichas_jugador, x, y, direccion)
        tablero.imprimir()
        print " "
        palabrascolocadas = palabrascolocadas + 1
        fichascolocadas= fichascolocadas + 7-(fichas_jugador.longitud())
        print " "
        fichas_jugador.darfichas( fichas_jugador.longitud() ,fichas_jugador, fichas)
        tf_fichas_jugador= fichas_jugador.getFrecuencias()
        print " "
        print "Tus fichas para jugar son: " + str(fichas_jugador)
        print " "
        print "Las palabras colocadas son: " + str(palabrascolocadas)
        print "Las fichas colocadas son: " + str(fichascolocadas)

    else:
        print""
        print "No es posible colocarla, intentalo de nuevo."
        
    print ""
    print "Escribe AYUDAPALABRA para ver las posibles palabras a colocar"
    print "Escribe AYUDACOLOCAR para ver las posibles palabras a colocar"
    print ""
    print "Dime la palabra que quieres colocar o la ayuda que quieres recibir:"
    primera = Palabra.leer_palabra()
    
    while (str(primera)== "AYUDAPALABRA" ) or (str(primera)== "AYUDACOLOCAR"):
        if (str(primera)== "AYUDAPALABRA" ):
            diccionario.mostrarPalabra(tf_fichas_jugador)
            print "Dime la palabra que quieres colocar:"
            primera = Palabra.leer_palabra()
         
        if (str(primera)== "AYUDACOLOCAR"):
            print "Dime la palabra que quieres que te ayude a colocar:"
            primera = Palabra.leer_palabra()
            print""
            tablero.mostrarcolocacion(primera, palabrascolocadas)
            print "Dime la palabra que quieres colocar:"
            primera = Palabra.leer_palabra()