from re import S
import numpy as np
import turtle
import os
import sys
from Nodo import Nodo
from email.mime import image


juego = np.array([


])
juego = np.loadtxt('matriz.txt', skiprows=0)  # Carga del txt
# 0=robot,1=roca,2=espacios disponibles,3=tiburon,4=torguda,5=dori,6=marlin,7=nemo,Acuaman=8
wn = turtle.Screen()  # crea la pantalla de la interfaz
wn.title("Juego de buscando a nemo")  # Le da el titulo a la ventana
wn.setup(width=500, height=500)  # le da las dimesiones a la ventana
wn.bgcolor('sky blue')  # le da el color de fondo

robot = turtle.Turtle()  # crea el objeto turtle a la ventana

dot_distance = 55  # distancia entre puntos
width = 6  # ancho de la matriz
height = 6  # largo de la matriz
robot.speed(50)  # velocidad de dibujado
robot.penup()  # levanta la pluma
robot.goto(-200, 200)  # cordenas de inicio para pintar
'''roca.speed(50)#velocidad de dibujado
roca.penup()# levanta la pluma 
roca.goto(-200,200)'''  # cordenas de inicio para pintar

for i in range(0, juego.shape[0]):
    for j in range(0, juego.shape[1]):

        robot.pendown()  # bajar la pluma

        if juego[i, j] == 0:
            robot.fillcolor('blue')  # rellena los cuadrados de color azul
        if juego[i, j] == 1:
            robot.fillcolor('coral')  # rellena los cuadrados de color azul
        if juego[i, j] == 2:
            robot.fillcolor('green')  # rellena los cuadrados de color azul
        if juego[i, j] == 3:
            robot.fillcolor('beige')  # rellena los cuadrados de color azul
        if juego[i, j] == 4:
            robot.fillcolor('azure')  # rellena los cuadrados de color azul
        if juego[i, j] == 5:
            robot.fillcolor('DarkGray')  # rellena los cuadrados de color azul
        if juego[i, j] == 6:
            # rellena los cuadrados de color azul
            robot.fillcolor('aquamarine')
        if juego[i, j] == 7:
            robot.fillcolor('pink')  # rellena los cuadrados de color azul
        if juego[i, j] == 8:
            robot.fillcolor('black')  # rellena los cuadrados de color azul

        robot.begin_fill()  # empieza a pintar
        robot.forward(50)  # traza una linea 50 pixeles
        robot.right(90)  # gira 90 grados el dibujado
        # se repite para completar el cuadrado
        robot.forward(50)
        robot.right(90)

        robot.forward(50)
        robot.right(90)

        robot.forward(50)
        robot.right(90)
        robot.end_fill()  # finaliza el rellenado

        robot.penup()  # termina de pintar
        robot.forward(dot_distance)  # separa los los dibujos del pinsel

    robot.backward(dot_distance*width)  # permite regresar al inicio el pinsel

    # permite que el pinsel baje (recuadros)
    robot.right(90)
    robot.forward(dot_distance)
    robot.left(90)


def busqueda_amplitud(juego):
    
    bot = turtle.Turtle()
    bot.speed(50)  # velocidad de dibujado
    bot.penup()  # levanta la pluma
    bot.goto(-200, 200)  # cordenas de inicio para pintar'''

    for i in range(0, juego.shape[0]):
        for j in range(0, juego.shape[1]):

            if juego[i, j] == 0:
                post_bot = (i, j)               
                juego[i, j] = 2  # Colocar la posición como un espacio libre

                '''bot.pendown()  # bajar la pluma
                # rellena los cuadrados de color azul
                bot.fillcolor('blue')
                bot.begin_fill()  # empieza a pintar
                bot.forward(50)  # traza una linea 50 pixeles
                bot.right(90)  # gira 90 grados el dibujado
                # se repite para completar el cuadrado
                bot.forward(50)
                bot.right(90)

                bot.forward(50)
                bot.right(90)

                bot.forward(50)
                bot.right(90)
                bot.end_fill()  # finaliza el rellenado

                bot.penup()  # termina de pintar
                # separa los los dibujos del pinsel
                bot.forward(dot_distance)

                # permite regresar al inicio el pinsel
                bot.backward(dot_distance*width)

                # permite que el pinsel baje (recuadros)
                bot.right(90)
                bot.forward(dot_distance)
                bot.left(90)
            
            robot.backward(dot_distance*width)  # permite regresar al inicio el pinsel

    # permite que el pinsel baje (recuadros)
            robot.right(90)
            robot.forward(dot_distance)
            robot.left(90)'''
            break  # Salga del for

            
    raiz = Nodo(
        juego,
        post_bot,
        (False, False, False),
        [post_bot],
        [post_bot]
    )
    cola = [raiz]
    nodos_expandidos = 1
    nodos_creados = 1
    while True:       
        nodo = cola.pop(0)  # quito el primero elemento
        nodos_expandidos += 1
        # Condicion de ganar
        if nodo.verificar_ganar():
            return nodo.recorrido, nodos_expandidos, nodos_creados

        hijos = nodo.generar_hijos()
        for h in hijos:
            if not(h.verificar_perdi()):  # Solo evaluo nodos en cuales no pierdo
                cola.append(h)
            nodos_creados += 1
        # Condición de no encontrar
        if len(cola) == 0:
            return None, nodos_expandidos, nodos_creados
        matriz = np.matrix(nodo.recorrido)
        print(matriz)

        bot = turtle.Turtle()

        dot_distance = 55  # distancia entre puntos
        width = 6  # ancho de la matriz
        height = 6  # largo de la matriz
        bot.speed(50)  # velocidad de dibujado
        bot.penup()  # levanta la pluma
        bot.goto(-200, 200) 
        for i in range(0, juego.shape[0]):
            for j in range(0, juego.shape[1]):

                bot.pendown()  # bajar la pluma

                if matriz[i, j] == 0:
                    bot.fillcolor('blue')  # rellena los cuadrados de color azul

                bot.begin_fill()  # empieza a pintar
                bot.forward(50)  # traza una linea 50 pixeles
                bot.right(90)  # gira 90 grados el dibujado
                # se repite para completar el cuadrado
                bot.forward(50)
                bot.right(90)

                bot.forward(50)
                bot.right(90)

                bot.forward(50)
                bot.right(90)
                bot.end_fill()  # finaliza el rellenado

                bot.penup()  # termina de pintar
                bot.forward(dot_distance)  # separa los los dibujos del pinsel

            bot.backward(dot_distance*width)  # permite regresar al inicio el pinsel

            # permite que el pinsel baje (recuadros)
            bot.right(90)
            bot.forward(dot_distance)
            bot.left(90)

   
        


def busqueda_profundidad(juego):
    for i in range(0, juego.shape[0]):
        for j in range(0, juego.shape[1]):
            if juego[i, j] == 0:
                post_bot = (i, j)
                juego[i, j] = 2  # Colocar la posición como un espacio libre
                break  # Salga del for

    raiz = Nodo(
        juego,
        post_bot,
        (False, False, False),
        [post_bot],
        [post_bot]

    )
    pila = [raiz]
    nodos_expandidos = 1
    nodos_creados = 1
    while True:

        nodo = pila.pop(-1)  # quito el primero elemento
        nodos_expandidos += 1
        # Condicion de ganar
        if nodo.verificar_ganar():
            return nodo.recorrido, nodos_expandidos, nodos_creados

        hijos = nodo.generar_hijos()
        for h in hijos:
            if not(h.verificar_perdi()):  # Solo evaluo nodos en cuales no pierdo
                pila.append(h)
            nodos_creados += 1
        # Condición de no encontrar
        if len(pila) == 0:
            return None, nodos_expandidos, nodos_creados


print(busqueda_amplitud(juego.copy()))
print(busqueda_profundidad(juego.copy()))
turtle.done()  # termina el trabajo


'''wn = turtle.Screen()#crea la pantalla de la interfaz
wn.title("Juego de buscando a nemo")#Le da el titulo a la ventana
wn.setup(width = 500, height=500)#le da las dimesiones a la ventana
wn.bgcolor('sky blue')#le da el color de fondo

robot = turtle.Turtle()#crea el objeto turtle a la ventana

dot_distance = 55#distancia entre puntos
width = 6# ancho de la matriz
height = 6# largo de la matriz
robot.speed(50)#velocidad de dibujado
robot.penup()# levanta la pluma 
robot.goto(-200,200)# cordenas de inicio para pintar
for y in range (height):# ciclo doble donde y  es la ultura
   for i in range(width): # ciclo doble donde i  es el ancho
     
        robot.pendown()#bajar la pluma
        robot.fillcolor('blue')#rellena los cuadrados de color azul
        robot.begin_fill()# empieza a pintar
        robot.forward(50)# traza una linea 50 pixeles
        robot.right(90)#gira 90 grados el dibujado
        #se repite para completar el cuadrado
        robot.forward(50)
        robot.right(90)

        robot.forward(50)
        robot.right(90)

        robot.forward(50)
        robot.right(90)
        robot.end_fill()#finaliza el rellenado
        
        robot.penup()# termina de pintar
        robot.forward(dot_distance)#separa los los dibujos del pinsel
    
   robot.backward(dot_distance*width)# permite regresar al inicio el pinsel

    # permite que el pinsel baje (recuadros)
   robot.right(90)
   robot.forward(dot_distance)#
   robot.left(90)

turtle.done()'''  # termina el trabajo

