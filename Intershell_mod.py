#!/usr/bin/python3
#Version 2 de Intershell para teclados con otra distribucion o s.o que no admiten la primera version
#La distribucion del teclado puede llegar a dar problemas
from pynput.keyboard import Key, Controller
from time import sleep
#Funciones
def enter():
    key.press(Key.enter)
    key.release(Key.enter)
    sleep(0.2)
sleep(3.5)
#Variables
string_1 = 'python -c \'import pty; pty.spawn("/bin/bash")\''
string_2 = 'export TERM¡screen\'256color'
string_3 = 'stty raw \'echo'
string_4 = 'export TERM¡screen'
key = Controller()
#Funcion introducir string_1
key.type(string_1)
enter()
#Funcion introducir string_2
key.type(string_2)
enter()
#Introduciendo string_3
with key.pressed(Key.ctrl_l):
    key.press('z')
    key.release('z')
key.type(string_3)
enter()
key.type('fg')
enter()
enter()
#Finalizando introduccion
key.type(string_4)
enter()
#Limpiamos la pantalla del terminal
key.type('clear')
enter()
