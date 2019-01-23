#! /usr/bin/env python
#-*- coding: UTF-8 -*-

import pygame, sys
from PyGUI.controles import *
from PyGUI.herramientas import *


'''Archivo principal de Laberintos v.1'''


pygame.init()

# Variables globales
FPS = 0
fps_font = Font('Default', Color.Goldenrod)
clock = pygame.time.Clock()
deltatime = 1




def show_info():
    fps_overlay = fps_font.render(str(int(FPS)), True)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = (0, 0) #(800, 800 *9/16) #  (mantiene una relacion 16:9)
                                            # 1366, 768 (resolucion de maquina HP)
    window_title = "Prueba GUI version alterna"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
    window_width, window_height = window.get_size()


def count_fps():
    global FPS, clock

    FPS = clock.get_fps()
    if FPS > 0:
        deltatime = 1 / FPS


def salir():
    global isRunning
    isRunning = False


# Creo la ventana de juego para tener ya algunas variables
create_window()


###############################################
#             Pantalla de inicio              #
###############################################

    #  Imagen de inicio
im = pygame.image.load('recursos/Laberinto3.png')
imgInicio = Image(im.get_rect(center = (window_width/2, 75)), 'imgportada', im)
del im

    #  Titulo del juego
lblTitulo_rect = (window_width/2-250, 175, 500,  60)
lblTitulo = Label(lblTitulo_rect, 'lbltitulo', 'LABERINTOS')
lblTitulo.border.show = False
lblTitulo.font = Font('Large', Color.DarkSeaGreen)
lblTitulo.background.normal_color = Color.Transparent
lblTitulo.background.hover_color = Color.Transparent
lblTitulo.background.down_color = Color.Transparent
#lblTitulo.midground.normal_color = Color.Transparent
lblTitulo.foreground.hover_color = Color.DarkSeaGreen
lblTitulo.foreground.down_color = Color.DarkSeaGreen

    #  Botones
anchoBoton = 250
altoBoton = 30

btnJugar_rect = (window_width/2-125,         345,  anchoBoton,  altoBoton)
btnJugar = Button(btnJugar_rect, "JUGAR", lambda: Screen.set_current('jugar'))
btnJugar.font = Font('Default', Color.DarkSeaGreen)
btnJugar.background.normal_color = Color.Transparent
btnJugar.background.hover_color = (25,25,25)
btnJugar.background.down_color = Color.Transparent
btnJugar.foreground.hover_color = Color.LawnGreen
btnJugar.foreground.down_color = Color.DarkSeaGreen

btnCreditos_rect = (window_width/2-125, 380,  anchoBoton,  altoBoton)
btnCreditos = Button(btnCreditos_rect, "CREDITOS", lambda: Screen.set_current('creditos'))
btnCreditos.font = Font('Default', Color.DarkSeaGreen)
btnCreditos.background.normal_color = Color.Transparent
btnCreditos.background.hover_color = (25,25,25)
btnCreditos.background.down_color = Color.Transparent
btnCreditos.foreground.hover_color = Color.LawnGreen
btnCreditos.foreground.down_color = Color.DarkSeaGreen

btnSalir_rect = (window_width/2-125,         415,  anchoBoton,  altoBoton)
btnSalir = Button(btnSalir_rect, "SALIR", salir)
btnSalir.font = Font('Default', Color.DarkSeaGreen)
btnSalir.background.normal_color = Color.Transparent
btnSalir.background.hover_color = (25,25,25)
btnSalir.background.down_color = Color.Transparent
btnSalir.foreground.hover_color = Color.LawnGreen
btnSalir.foreground.down_color = Color.DarkSeaGreen

    #  Creo la pantalla
main = Screen('main')
main.background_color = (20,20,20)
main.addControls(imgInicio, lblTitulo, btnJugar, btnCreditos, btnSalir)
main.update()


###############################################
#             Pantalla de creditos            #
###############################################

    # Boton volver al main
btnVolver_rect = (window_width-30-90, 5, 90, 30)
btnVolver = Button(btnVolver_rect, 'VOLVER', lambda: Screen.set_current('main'))
btnVolver.font = Font('Small', Color.DarkSeaGreen)
btnVolver.background.normal_color = Color.Transparent
btnVolver.background.hover_color = Color.Transparent
btnVolver.background.down_color = Color.Transparent
btnVolver.foreground.hover_color = Color.LawnGreen
btnVolver.foreground.down_color = Color.DarkSeaGreen

    # Imagen de firma
im = pygame.image.load('recursos/logo_mlp.png')
imgFirma = Image(im.get_rect(center = (window_width/2, window_height/2 - 150)), 'firma', im)
del im
    
    #  Creditos
lblCreditos_rect = (0, imgFirma.top + imgFirma.get_height() ,  window_width,  40)
lblCreditos = Label(lblCreditos_rect, 'lblcreditos', u'Idea, diseño y programación por Martincholp')
lblCreditos.border.show = False
lblCreditos.font = Font('Small', Color.DarkSeaGreen)
lblCreditos.background.normal_color = Color.Transparent
lblCreditos.background.hover_color = Color.Transparent
lblCreditos.background.down_color = Color.Transparent
lblCreditos.foreground.hover_color = Color.DarkSeaGreen
lblCreditos.foreground.down_color = Color.DarkSeaGreen

    #  E-mail
lblEmail_rect = (0, lblCreditos.top + lblCreditos.get_height() ,  window_width,  40)
lblEmail = Label(lblEmail_rect, 'lblemail', 'martincholp@hotmail.com')
lblEmail.border.show = False
lblEmail.font = Font('Small', Color.DarkSeaGreen)
lblEmail.background.normal_color = Color.Transparent
lblEmail.background.hover_color = Color.Transparent
lblEmail.background.down_color = Color.Transparent
lblEmail.foreground.hover_color = Color.DarkSeaGreen
lblEmail.foreground.down_color = Color.DarkSeaGreen

    #  Fecha
lblFecha_rect = (0, lblEmail.top + lblEmail.get_height() ,  window_width,  40)
lblFecha = Label(lblFecha_rect, 'lblfecha', 'Enero 2019')
lblFecha.border.show = False
lblFecha.font = Font('Small', Color.DarkSeaGreen)
lblFecha.background.normal_color = Color.Transparent
lblFecha.background.hover_color = Color.Transparent
lblFecha.background.down_color = Color.Transparent
lblFecha.foreground.hover_color = Color.DarkSeaGreen
lblFecha.foreground.down_color = Color.DarkSeaGreen

    #  Creo la pantalla
creditos = Screen('creditos')
creditos.background_color = (20,20,20)
creditos.addControls(imgFirma, lblCreditos, lblEmail, lblFecha, btnVolver)
creditos.update()

###############################################
#             Pantalla de juego               #
###############################################

    # Zona de juego (actualmente la represento con un simple control vacio)
zonaJuego_rect = (30, 40, window_width - 60, window_height - 70)
zonaJuego = Control(zonaJuego_rect, "zonaJuego")

    # Boton volver al main
btnVolver2_rect = (window_width-30-90, 5, 90, 30)
btnVolver2 = Button(btnVolver_rect, 'VOLVER', lambda: Screen.set_current('main'))
btnVolver2.font = Font('Small', Color.DarkSeaGreen)
btnVolver2.background.normal_color = Color.Transparent
btnVolver2.background.hover_color = Color.Transparent
btnVolver2.background.down_color = Color.Transparent
btnVolver2.foreground.hover_color = Color.LawnGreen
btnVolver2.foreground.down_color = Color.DarkSeaGreen

    #  Creo la pantalla
juego = Screen('jugar')
juego.background_color = (20,20,20)
juego.addControls(zonaJuego, btnVolver2) 
juego.update()




# Establezco la pantalla inicial
Screen.set_current('main')




# INICIALIZO GUI

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:            

            if event.key == pygame.K_ESCAPE:
                isRunning = False
                
            elif event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

            elif event.key == pygame.K_TAB:
                 # cambio el control en foco con tab. Para el control anterior uso shift+tab
                if pygame.key.get_mods() == pygame.KMOD_LSHIFT or pygame.key.get_mods() == pygame.KMOD_RSHIFT or pygame.key.get_mods() == 8193 or pygame.key.get_mods() == 8194 :  # Son los shift con los bloq mayusc activado
                    Screen.get_current().focus_prev()
                else:
                    Screen.get_current().focus_next()
    
            elif event.key == pygame.K_F1:  #  Pantalla nro 1
                Screen.set_current('main')

            elif event.key == pygame.K_F2:  #  Pantalla nro 2
                Screen.set_current('creditos')

            elif event.key == pygame.K_F3:  #  Pantalla nro 3
                Screen.set_current('jugar')


            else:
                # Para cualquier otra tecla se la doy al control en foco para que lo procese
                contAct = Screen.get_current().get_focus()
                if contAct != None:
                    contAct.keydown(event)



        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle left button click events
            for ctl in Screen.get_current().get_controls():
                if ctl.click(event):
                    break
        
        #elif event.type == pygame.MOUSEMOTION:


    # Process menu
    window.fill(Screen.get_current().background_color)

    Screen.get_current().render(window)
    

    show_info()
    
    pygame.display.update()

    clock.tick()
    count_fps()



pygame.quit()
sys.exit()