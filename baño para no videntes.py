#!/usr/bin/env python


#inicializaciones y valores definidos.
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.gpio import CharLCD
from RPi import GPIO
import time
import threading
import os

#Archivos de audio
file = "/home/pi/Desktop/lector.mp3"
file2="/home/pi/Desktop/linea.mp3"
file3="/home/pi/Desktop/entrada.mp3"
file4="/home/pi/Desktop/48.mp3"
file5="/home/pi/Desktop/30.mp3"
file6="/home/pi/Desktop/ingresoalbañonovidente"
file7="/home/pi/Desktop/3.mp3"
file8="/home/pi/Desktop/salidamedio..mp3"
file9="/home/pi/Desktop/cerrar.mp3"
file10="/home/pi/Desktop/intrucciones.mp3"
file11="/home/pi/Desktop/salida.mp3"
file12="/home/pi/Desktop/tarjetasalisa.mp3"
file13="/home/pi/Desktop/bañonormal"
file14="/home/pi/Desktop/adios.mp3"
file15="/home/pi/Desktop/20cm.mp3"
file16="/home/pi/Desktop/salidanoviden.mp3"
file17="/home/pi/Desktop/lectura1salidano.mp3"
file18="/home/pi/Desktop/39centrino"
file19="/home/pi/Desktop/lavatorionovidente"
file20="/home/pi/Desktop/novisa"
file21="/home/pi/Desktop/guiaizq"
file22="/home/pi/Desktop/lectorno"
file23="/home/pi/Desktop/taza"


#Definicion entradas y salidas

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Primera tira led
GPIO.setup(37, GPIO.OUT)#color azul
GPIO.setup(33, GPIO.OUT)#color verde

#Segundas 2 tiras led
GPIO.setup(15, GPIO.OUT)#color azul
GPIO.setup(13, GPIO.OUT)#color verde

#Led lavatorio
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

#Tercera tira led
GPIO.setup(18, GPIO.OUT)#color azul
GPIO.setup(29, GPIO.OUT)#color verde

#Entradas sensor de puerta e infrarojo
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)

#Entrada y salida sensor utrasonico
GPIO_TRIGGER=8                    #Usamos el pin GPIO 25 como TRIGGER
GPIO_ECHO=10                   #Usamos el pin GPIO 7 como ECHO
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)   #Configuramos Trigger como salida
GPIO.setup(GPIO_ECHO,GPIO.IN)       #Configuramos Echo como entrada
GPIO.output(GPIO_TRIGGER,False)     #Ponemos el pin 25 como LOW

#valores lcd

lcd =CharLCD (pin_rs = 40, pin_rw = None, pin_e = 38, pins_data = [36,32,26,31],
numbering_mode =GPIO.BOARD)         #valores iniciales de lcd


#valores lector rc522
reader = SimpleMFRC522()

#Numeros de tarjetas id.
visionreducida=1070585815161
novidente=284593894443



#interrupcciones para ejecutar hilos y sus funciones.

def Timer_Interrumpt():

    print("interrupcion por tiempo")
    lcd . crlf ()
    mensajecon()
    threading.Timer(0.5,Timer_Interrumpt).start()

def Timer_Interrumpt2():
    print("interrupcion89or tiempo 2")
    vozen1()
    threading.Timer(0.5,Timer_Interrumpt2).start(1)


def Timer_Interrumpt3():
    print("interrupcion tiempo 3")
    sensorinfra()
    threading.Timer(0.5,Timer_Interrumpt3).start()x03

def Timer_Interrumpt4():
    print("interrupcion tiempo 4")

    threading.Timer(0.5,Timer_Interrumpt4).start(1)


#funciones pantalla LCD

def mensajecon():
    lcd.write_string ( "Favor No destruir\ n \ r esta area")
    time.sleep()
    lcd.clear()

#Funciones Voces

def vozen():
    os.system("mpg123 " + file)
def vozenno():
    os.system("mpg123 " + file2)
def vozen1():
    os.system("mpg123 " + file3)
def vozeno1():
    os.system("mpg123 " + file4)
def vozeno2():
    os.system("mpg123 " + file5)
def entradanovidente():
    os.system("mpg123 " + file6)
def vozeno4():
    os.system("mpg123 " + file7)
def vozenno5():
    os.system("mpg123 " + file15)
def vozsa():
    os.system("mpg123 " + file8)
def vozpuertace():
    os.system("mpg123 " + file9)
def vozintrucci():
    os.system("mpg123 " + file10)
def vozsaba():
    os.system("mpg123 " + file11)
def virajeizq():
    os.system("mpg123 " + file12)
def tarjesa():
    os.system("mpg123 " + file13)
def adios():
    os.system("mpg123 " + file14)
def salidanovinde():
    os.system("mpg123 " + file16)
def salidano1():
    os.system("mpg123 " + file17)
def izquierdano():
    os.system("mpg123 " + file18)
def lavatoriosalida():
    os.system("mpg123 " + file19)
def novisa():
    os.system("mpg123 " + file20)
def guiaizq():
    os.system("mpg123 " + file21)
def lectorno():
    os.system("mpg123 " + file22)
def taza():
    os.system("mpg123 " + file23)


#Funciones sensores ultrasonicos


def ultrasonico2():                      #avisa distacias no videntes.

    while True:                          #Iniciamos un loop infinito
        apagar1()
        apagar2()
        GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(0.00001)              #Una pequeñña pausa
        GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
        start = time.time()              #Guarda el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
            stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
        elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
        distancia2 = (elapsed * 34300)/2  #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        print ("{:.0f}".format(distancia2))                #Devolvemos la distancia (en centímetros) por pantalla
        time.sleep(0.3)         #tiempo de muestreo

        if distancia2 <= 44 and distancia2 >= 40  :               #condicion de distacia
            vozeno1()                    #inicia voz para aletar donde esta lector de tarjetas.
                                                #iniica funcion para leer tarjeta o llavero rf

        if distancia2 >=30 and distancia2 <=  34:               #condicion de distacia
            vozeno2()

        if distancia2 <=15 and distancia2 >= 10:  #condicion de distacia
            entradanovidente()
            taza()
            print("hola")
            return

def ultrasonico3():     #final salida vision reducida.

    while True:                          #Iniciamos un loop infinito
        GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(0.00001)              #Una pequeñña pausa
        GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
        start = time.time()              #Guarda el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
            stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
        elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
        distancia3 = (elapsed * 34300)/2  #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        print ("{:.0f}".format(distancia3)) #Devolvemos la distancia (en centímetros) por pantalla
        time.sleep(1)                       #tiempo de muestreo

        if distancia3 >= 28 and distancia3 <= 39: #condicion de distacia
            virajeizq()


        if distancia3 >= 45 and distancia3 <= 48:
            tarjesa()
            return

def ultrasonico4():         #final salida lavatorio no vidente.

    while True:             #Iniciamos un loop infinito
        apagar1()
        apagar2()
        GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(0.00001)              #Una pequeñña pausa
        GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
        start = time.time()              #Guarda el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
            stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
        elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
        distancia4 = (elapsed * 34300)/2  #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        print ("{:.0f}".format(distancia4))                #Devolvemos la distancia (en centímetros) por pantalla
        time.sleep(0.3)
        if distancia4 >= 10 and distancia4 <= 20  :             #condicion de distacia
            salidano1()            #iniica funcion para leer tarjeta o llavero rf
        if distancia4 >= 30 and distancia4 <= 35  :
            izquierdano()
            lavatoriosalida()
            return
def ultrasonico5():         #final salida no vidente.

    while True:             #Iniciamos un loop infinito
        apagar1()
        apagar2()
        GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(0.00001)              #Una pequeñña pausa
        GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
        start = time.time()              #Guarda el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
            stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
        elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
        distancia5 = (elapsed * 34300)/2  #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        print ("{:.0f}".format(distancia5))                #Devolvemos la distancia (en centímetros) por pantalla
        time.sleep(1)
        if distancia5 >= 35 and distancia5 <= 40  :
            guiaizq()
        if distancia5 >= 40 and distancia5 <= 48 :
            lectorno()
            return

#funciones de entrada
def entrada():                                  #funcion entrada.
    while GPIO.input(12) ==  False:
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
        threading.Timer(0.5,Timer_Interrumpt2).start()
        time.sleep(6)
        time.sleep(2)
        GPIO.output(33,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(33,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(33,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(33,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(33,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(33,GPIO.HIGH)
        time.sleep(2)
        vozpuertace()
        time.sleep(3)
        taza()
    return

#Funciones de puerta cerrada
def puertacerrada():
    while GPIO.input(12) == True:
        time.sleep(0.3)
        apagar1()
        lcd.write_string(u'ocupado' )
        time.sleep(0.3)
        lcd.clear()
    time.sleep(0.3)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(29,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(29,GPIO.LOW)
    vozsa()
    time.sleep(0.3)
    GPIO.output(29,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(29,GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(29,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(29,GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(29,GPIO.HIGH)
    vozintrucci()
    vozsaba()
    return
def salidanovidente():

    time.sleep(0.3)
    salidanovinde()
    ultrasonico4()

def salidavisionreducida():
    while True:

        id, text = reader.read()                #funcion reader.read() lee la informacion de la tarjeta y la guarda en la variable ID.
        if id == visionreducida:                #Si ID es igual a la informacion que tiene la tarjeta ingresada entra a estas lineas de codigo.
            print("visionreducida saliendo")
            return

def banosalidano():
    while True:

        id, text = reader.read()           #funcion reader.read() lee la informacion de la tarjeta y la guarda en la variable ID.
        if id == novidente:                #Si ID es igual a la informacion que tiene la tarjeta ingresada entra a estas lineas de codigo.
            print("novidente saliendo")
            return

def lavatoriosalir():
    while True:
        if GPIO.input(16) == False:
            print("detencion2")
            novisa()
            return

#funciones sensor infrarojo

def sensorinfra():
    if GPIO.input(16) == False:
        print("detencion")
        GPIO.output(3,GPIO.HIGH)
        #GPIO.output(5,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
    else:
        GPIO.output(3,GPIO.LOW)
        #GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)

#Funciones apagar rutinas

def apagar1():
    GPIO.output(33,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
def apagar2():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
def banonormalvr():
    apagar1()
    apagar2()
    lcd.clear()

def banonorma():
    print("visionreducida")
    apagar1()
    apagar2()
    lcd.clear()

#Funcion principal

while True :
    lcd.clear()
    threading.Timer(0.5,Timer_Interrumpt).start()
    threading.Timer(0.5,Timer_Interrumpt3).start()
    apagar1()                               #mantiene luces apagadas
    apagar2()                               #mantiene luces apagadas
    id, text = reader.read()
    if id == visionreducida:                #Si ID es igual a la informacion que tiene la tarjeta ingresada entra a estas lineas de codigo.
        print("visionreducida")
        entrada()
        puertacerrada()
        ultrasonico3()
        salidavisionreducida()
        adios()
        banonormalvr()

    if id == novidente:     #Condicion si id es igual a la informacion que tiene la tarjeta de no videntes corre las lines de codigo que corresponde.
        print("novidente")  #imprime en el copilador no vidente solo parfa guiar.
        time.sleep(1)
        vozenno()
        ultrasonico2()
        print("hola 2")
        print("hola4")
        while GPIO.input(12) == True:
            print("hola 3")
            lcd.write_string(u'ocupado')
            time.sleep(0.3)
            lcd.clear()
        salidanovidente()
        lavatoriosalir()
        ultrasonico5()
        banosalidano()
        adios()
        banonormalvr()

GPIO.cleanup()