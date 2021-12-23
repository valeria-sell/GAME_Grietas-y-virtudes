import pygame
import random
import time
from pygame.locals import *
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((750,600))
pygame.display.set_caption("Grietas y Virtudes")

#-----------------IMAGENES------------------------------------------------------------------------------------------------------------------------
backimage = pygame.image.load("map.jpeg")
backimage = pygame.transform.scale(backimage, (600, 600))

river = pygame.image.load("rio.jpg")
river = pygame.transform.scale(river, (150, 600))

arrow = pygame.image.load("arrow.png")
arrow = pygame.transform.scale(arrow, (50, 50))

home = pygame.image.load("main.jpg")
home = pygame.transform.scale(home, (600, 600))

_P1 = pygame.image.load("pin1.png")
_P1 = pygame.transform.scale(_P1, (40, 50))

_P2 = pygame.image.load("pin2.png")
_P2 = pygame.transform.scale(_P2, (40, 50))

_P3 = pygame.image.load("pin3.png")
_P3 = pygame.transform.scale(_P3, (60, 50))

_P4 = pygame.image.load("pin4.png")
_P4 = pygame.transform.scale(_P4, (60, 70))

#-----------------MATRIZ DE TABLERO---------------------------------------------------------------------------------------------------------------
#FORMATO [NUM DE CASILLA, TIPO DE CASILLA, CASILLA DIRIGIDA]
#TIPOS: 3 ESTANDAR, 1 PECADO, 2 VIRTUD

_TABLERO = [
 [100,0,0], [99,1,15],  [98,0,0],   [97,0,0],   [96,0,0],   [95,0,0],   [94,0,0],   [93,0,0],   [92,0,0],   [91,1,66],  #FILA 10
 [81,0,0],  [82,2,93],  [83,0,0],   [84,0,0],   [85,0,0],   [86,0,0],   [87,1,51],  [88,0,0],   [89,0,0],   [90,0,0],   #FILA 9
 [80,1,2],  [79,0,0],   [78,0,0],   [77,2,95],  [76,0,0],   [75,0,0],   [74,0,0],   [73,0,0],   [72,0,0],   [71,1,34],  #FILA 8
 [61,0,0],  [62,0,0],   [63,0,0],   [64,0,0],   [65,1,50],  [66,0,0],   [67,0,0],   [68,0,0],   [69,0,0],   [70,0,0],   #FILA 7
 [60,0,0],  [59,0,0],   [58,0,0],   [57,0,0],   [56,0,0],   [55,0,0],   [54,0,0],   [53,0,0],   [52,0,0],   [51,0,0],   #FILA 6
 [41,0,0],  [42,0,0],   [43,0,0],   [44,0,0],   [45,0,0],   [46,0,0],   [47,2,76],  [48,0,0],   [49,0,0],   [50,0,0],   #FILA 5
 [40,0,0],  [39,0,0],   [38,0,0],   [37,1,13],  [36,0,0],   [35,0,0],   [34,0,0],   [33,0,0],   [32,0,0],   [31,0,0],   #FILA 4
 [21,0,0],  [22,0,0],   [23,0,0],   [24,0,0],   [25,2,67],  [26,0,0],   [27,0,0],   [28,0,0],   [29,0,0],   [30,0,0],   #FILA 3
 [20,2,98], [19,0,0],   [18,0,0],   [17,0,0],   [16,0,0],   [15,0,0],   [14,0,0],   [13,0,0],   [12,0,0],   [11,0,0],   #FILA 2
 [1,0,0],   [2,0,0],    [3,0,0],    [4,2,79],   [5,0,0],    [6,0,0],    [7,0,0],    [8,0,0],    [9,0,0],    [10,2,28]]  #FILA 1

#-----------------MATRIZ DE POSICIONES------------------------------------------------------------------------------------------------------------
#CASILLA,X,Y
_COORDENADAS = [
    [1,170,410],[2,230,410],[3,288,410],[4,340,410],[5,392,410],[6,448,410],[7,500,410],[8,554,410],[9,609,410],
    [10,668,410],[11,668,367],[12,608,367],[13,554,367],[14,497,367],[15,448,367],[16,392,367],[17,340,367],[18,290,367],[19,230,367],
    [20,170,367],[21,170,320],[22,230,320],[23,290,320],[24,340,320],[25,392,320],[26,448,320],[27,497,320],[28,552,320],[29,608,320],
    [30,668,320],[31,668,267],[32,605,267],[33,552,267],[34,497,267],[35,448,267],[36,392,267],[37,340,267],[38,290,267],[39,230,267],
    [40,170,267],[41,170,220],[42,230,220],[43,290,220],[44,340,220],[45,392,220],[46,448,220],[47,497,220],[48,552,220],[49,605,220],
    [50,668,220],[51,668,170],[52,605,170],[53,552,170],[54,497,170],[55,448,170],[56,392,170],[57,340,157],[58,290,170],[59,230,170],
    [60,170,170],[61,170,145],[62,230,145],[63,290,145],[64,340,145],[65,392,145],[66,448,145],[67,497,145],[68,553,145],[69,608,145],
    [70,668,145],[71,668,79],[72,605,79],[73,552,79],[74,497,79],[75,448,79],[76,392,79],[77,340,79],[78,290,79],[79,230,79],
    [80,170,79],[81,170,30],[82,230,30],[83,290,30],[84,340,30],[85,392,30],[86,448,30],[87,497,30],[88,552,30],[89,615,30], 
    [90,668,30],[91,668,0],[92,605,0],[93,552,0],[94,497,0],[95,448,0],[96,392,0],[97,340,0],[98,290,0],[99,230,0],[100,170,0]]
#-----------------VAR DE FONDO--------------------------------------------------------------------------------------------------------------------
_FX = 150
_FY = 0

#-----------------POS DE ICONOS DE JUGADORES-------------------------------------------------------------------------------------------------------
_P1X = 103
_P1Y = 340

_P2X = 105
_P2Y = 400

_P3X = 95
_P3Y = 450

_P4X = 90
_P4Y = 500

#-----------------SET BOTON DE DADO---------------------------------------------------------------------------------------------------------------
lanzaDado = pygame.Rect(10,50,40,40)

#-----------------FUENTES DE TEXTO----------------------------------------------------------------------------------------------------------------
fuente1 = pygame.font.SysFont("arial",25)
fuente2 = pygame.font.SysFont("arial",20)
fuente3 = pygame.font.SysFont("arial",25, True,False)

#-----------------FUNCIONES AUXILIARES-------------------------------------------------------------------------------------------------------------
def fondo():
    screen.blit(backimage,(_FX,_FY))
    screen.blit(river,(0,0))
    screen.blit(arrow, (10,50))

def player1(x,y):
    screen.blit(_P1, (x,y))

def player2(x,y):
    screen.blit(_P2, (x,y))

def player3(x,y):
    screen.blit(_P3, (x,y))

def player4(x,y):
    screen.blit(_P4, (x,y))

#obtiene un numero al azar y muestra la imagen correspondiente
def lanzarDado():
    num_obtenido = random.randint(1,6)
    if num_obtenido == 1:
        dado = pygame.image.load("d1.png")
    elif num_obtenido == 2:
        dado = pygame.image.load("d2.png")
    elif num_obtenido == 3:
        dado = pygame.image.load("d3.png")
    elif num_obtenido == 4:
        dado = pygame.image.load("d4.png")
    elif num_obtenido == 5:
        dado = pygame.image.load("d5.png")
    elif num_obtenido == 6:
        dado = pygame.image.load("d6.png")
    return (dado, num_obtenido)

#pone iconos de jugadores en pantalla
def jugadores(n):
    if n >= 1:
        mss1 = fuente3.render("Jugador 1", True,(0,174,88))
        screen.blit(mss1,[2,351])
        player1(_P1X,_P1Y)
    if n >= 2:
        mss2 = fuente3.render("Jugador 2", True,(226,82,47))
        screen.blit(mss2,[2,400])
        player2(_P2X,_P2Y)
    if n >= 3:
        mss3 = fuente3.render("Jugador 3", True,(0,163,225))
        screen.blit(mss3,[2,453])
        player3(_P3X,_P3Y)
    if n >= 4:
        mss4 = fuente3.render("Jugador 4", True,(255,255,255))
        screen.blit(mss4,[2,510])
        player4(_P4X,_P4Y)

#setea la lista de jugadores activos
#los valores son [numero, resultado del dado actual, salio del rio o no, casilla en la que se encuentra]
def set_jugadoresactivos(n):
    if n >= 1:
        _JUGADORESACTIVOS.insert(0,["Jugador 1", 0, False, 0])
    if n >= 2:
        _JUGADORESACTIVOS.insert(1,["Jugador 2", 0, False, 0])
    if n >= 3:
        _JUGADORESACTIVOS.insert(2,["Jugador 3", 0, False, 0])
    if n >= 4:
        _JUGADORESACTIVOS.insert(3,["Jugador 4", 0, False, 0])
    print("Se inicia la partida con los siguientes jugadores: ",_JUGADORESACTIVOS)

def check_repeticiones(jugadores_listos, num_obtenido): 
    global _JUGADORESACTIVOS
    for i in range(jugadores_listos):
        if num_obtenido in _JUGADORESACTIVOS[i]:
            return False
    return True

def sort_jugadores():
    global _JUGADORESACTIVOS
    _JUGADORESACTIVOS.sort(key=lambda k: k[1], reverse=True)
    print("Orden de jugadores", _JUGADORESACTIVOS)

def avanza_turno(n):
    global _CANTDEJUGADORES
    if n<_CANTDEJUGADORES-1:
        n+=1
    else:
        n = 0
    return n

#revisa si la casilla es un pecado o virtud
def checkfor_casillainteractiva(n):
    global _TABLERO
    for i in range(100):
        if _TABLERO[i][0] == n:
            if _TABLERO[i][1] == 0:
                return (False, 1)
            elif _TABLERO[i][1] == 1:
                print("La casilla es un pecado. Retrocede")
                alerta2 = fuente1.render("Cayó en pecado! Retrocede", True,(0,0,0))
                screen.blit(alerta2,[200,550])
                return (True, _TABLERO[i][2])
            elif _TABLERO[i][1] == 2:
                print("La casilla es una virtud. Avanza")
                alerta2 = fuente1.render("Una virtud! Avanza", True,(0,0,0))
                screen.blit(alerta2,[200,550])
                return (True, _TABLERO[i][2])
    return (False, 3)

def move_jugador(info):
    global _TABLERO, _P1X, _P1Y, _P2X, _P2Y, _P3X, _P3Y, _P4X, _P4Y
    casilla = info[3]
    jugador = define_jugador(info[0])
    #funcion auxiliar para poner posiciones
    x,y = place_jugador(casilla)
    if jugador == 1:
        _P1X = x
        _P1Y = y
        
    elif jugador == 2:
        _P2X = x
        _P2Y = y
        
    elif jugador == 3:
        _P3X = x
        _P3Y = y
        
    else:
        _P4X = x
        _P4Y = y
    jugadores(_CANTDEJUGADORES)

def move_ganador(casilla, jugador):
    x,y = place_jugador(casilla)
    if jugador == 1:
        _P1X = x
        _P1Y = y
        
    elif jugador == 2:
        _P2X = x
        _P2Y = y
        
    elif jugador == 3:
        _P3X = x
        _P3Y = y
        
    else:
        _P4X = x
        _P4Y = y
    jugadores(_CANTDEJUGADORES)

    

def define_jugador(jugador):
    #recibe _JUGADORESACTIVOS[_TURNO][0]
    global _JUGADORESACTIVOS
    if jugador == "Jugador 1":
        return 1
    elif jugador == "Jugador 2":
        return 2
    elif jugador == "Jugador 3":
        return 3
    else:
        return 4

def place_jugador(casilla):
    global _COORDENADAS
    for i in range(99):
        if _COORDENADAS[i][0]==casilla:
            x = _COORDENADAS[i][1]
            y = _COORDENADAS[i][2]
            return (x,y)
        
#--------------FUNCIONes PARA ESCRITURA Y LECTURA DE ARCHIVOS-----------------------------------------------------------------------------------
def guardar_partida():
    archivo = open("partidaguardada.txt","w+")
    archivo.write(str(_CANTDEJUGADORES)+"\n")
    archivo.write(str(_P1X)+"\n")
    archivo.write(str(_P1Y)+"\n")
    archivo.write(str(_P2X)+"\n")
    archivo.write(str(_P2Y)+"\n")
    archivo.write(str(_P3X)+"\n")
    archivo.write(str(_P3Y)+"\n")
    archivo.write(str(_P4X)+"\n")
    archivo.write(str(_P4Y)+"\n")
    archivo.write(str(_TURNO)+"\n")
    archivo.write(str(_ORDENASIGNADO)+"\n")
    for i in _JUGADORESACTIVOS:
        for j in i:
            archivo.write(str(j)+"\n")
    archivo.close() 

def cargar_partida():
    global _CANTDEJUGADORES, _JUGADORESACTIVOS, _ORDENASIGNADO, _JUGADORESASIGNADOS, _TURNO, _P1X, _P1Y, _P2X, _P2Y, _P3X, _P3Y, _P4X, _P4Y
    with open("partidaguardada.txt") as f:
        lines = f.read()
        first = lines.split('\n', 1)[0]

    _CANTDEJUGADORES = int(first)

    with open("partidaguardada.txt", "r") as f:
        data = f.readlines()

    _P1X = int(data[1][:-1])
    _P1Y = int(data[2][:-1])
    _P2X = int(data[3][:-1])
    _P2Y = int(data[4][:-1])
    _P3X = int(data[5][:-1])
    _P3Y = int(data[6][:-1])
    _P4X = int(data[7][:-1])
    _P4Y = int(data[8][:-1])
    _TURNO = int(data[9][:-1])
    _ORDENASIGNADO = data[10][:-1]
    if _ORDENASIGNADO == "True":
        _ORDENASIGNADO = True
    else:
        _ORDENASIGNADO = False
    _JUGADORESACTIVOS = []    
    if _CANTDEJUGADORES >= 1:
        _JUGADORESACTIVOS.insert(0,[data[11][:-1], int(data[12][:-1]), data[13][:-1], int(data[14][:-1])])
    if _CANTDEJUGADORES >= 2:
        _JUGADORESACTIVOS.insert(1,[data[15][:-1], int(data[16][:-1]), data[17][:-1], int(data[18][:-1])])
    if _CANTDEJUGADORES >= 3:
        _JUGADORESACTIVOS.insert(2,[data[19][:-1], int(data[20][:-1]), data[21][:-1], int(data[22][:-1])])
    if _CANTDEJUGADORES >= 4:
        _JUGADORESACTIVOS.insert(3,[data[23][:-1], int(data[24][:-1]), data[25][:-1], int(data[26][:-1])])

#--------------VARIABLES DE PARTIDA--------------------------------------------------------------------------------------------------------------
_CANTDEJUGADORES = 4
_JUGADORESACTIVOS = []
_ORDENASIGNADO = False
_JUGADORESASIGNADOS = 0
_TURNO = 0

#--------------MAIN LOOP-------------------------------------------------------------------------------------------------------------------------
def main():
    global _CANTDEJUGADORES, _JUGADORESACTIVOS, _ORDENASIGNADO, _JUGADORESASIGNADOS, _TURNO
    mixer.init()
    mixer.music.load('music.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    set_jugadoresactivos(_CANTDEJUGADORES)
    
    running = True
    
    while running:
        screen.fill((221,221,221))
        fondo()
        jugadores(_CANTDEJUGADORES)
        #cargar_partida()
        #print("Se inicia partida con los siuientes jugadores: ", _JUGADORESACTIVOS)
        label_turno = _JUGADORESACTIVOS[_TURNO][0]
        mssturno = fuente1.render("Es el turno del", True,(255,255,255))
        screen.blit(mssturno,[5,10])
        mssturno = fuente1.render(label_turno, True,(255,255,255))
        screen.blit(mssturno,[50,30])
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                
                if lanzaDado.collidepoint(mouse_position):
                    lanzarDado()
                    #asigna las var obtenidas desde la funcion
                    dado, num_obtenido = lanzarDado()
                    screen.blit(dado,(20,120))
                    
                    print("Lanza dado, num obtenido: ", num_obtenido)
                    
                    if _ORDENASIGNADO == False:
                        
                        #jugadores lanzan dado para setear el orden
                        if _JUGADORESASIGNADOS == len(_JUGADORESACTIVOS):
                            _ORDENASIGNADO = True
                            
                        elif _JUGADORESASIGNADOS != _JUGADORESACTIVOS:
                            if check_repeticiones(_JUGADORESASIGNADOS,num_obtenido):
                                _JUGADORESACTIVOS[_JUGADORESASIGNADOS][1] = num_obtenido
                                _JUGADORESASIGNADOS += 1
                                sort_jugadores()
                                _TURNO = avanza_turno(_TURNO)
                                
                            else: 
                                print("Otro jugador ya lanzo ese numero, debe intentar de nuevo.")
                                alerta = fuente1.render("Empatado con otro jugador", True,(0,0,0))
                                screen.blit(alerta,[200,500])
                                alerta2 = fuente1.render("Lance el dado de nuevo", True,(0,0,0))
                                screen.blit(alerta2,[200,550])
                                
                    if _ORDENASIGNADO == True:
                        #empieza el juego propiamente-----------------------------------------------

                        #revisa si sigue o no en el rio estigia
                        if _JUGADORESACTIVOS[_TURNO][2]:
                            #juega normal
                            if num_obtenido == 6:
                                print("Es un 6. Juega de nuevo")
                                alerta = fuente1.render("Jugó un 6. Puede jugar nuevamente,", True,(0,0,0))
                                screen.blit(alerta,[200,550])
                                _JUGADORESACTIVOS[_TURNO][3] += num_obtenido
                                if _JUGADORESACTIVOS[_TURNO][3] > 100:
                                #Ups, no cayo exacto. Retrocede las casillas debidas
                                    dif = _JUGADORESACTIVOS[_TURNO][3]-100
                                    _JUGADORESACTIVOS[_TURNO][3] = 100 - dif
                                    move_jugador(_JUGADORESACTIVOS[_TURNO])
                                    cas_interactiva, num = checkfor_casillainteractiva(_JUGADORESACTIVOS[_TURNO][3])
                                    if cas_interactiva:
                                        _JUGADORESACTIVOS[_TURNO][3] = num
                                        move_jugadoor(_JUGADORESACTIVOS[_TURNO])
                                    print(_JUGADORESACTIVOS[_TURNO])
                                
                                move_jugador(_JUGADORESACTIVOS[_TURNO])
                                cas_interactiva, num = checkfor_casillainteractiva(_JUGADORESACTIVOS[_TURNO][3])
                                if cas_interactiva:
                                    _JUGADORESACTIVOS[_TURNO][3] = num
                                    move_jugador(_JUGADORESACTIVOS[_TURNO])
                                    
                                print(_JUGADORESACTIVOS[_TURNO]) 
                                if _JUGADORESACTIVOS[_TURNO][3] == 100:
                                    ganador = define_jugador(_JUGADORESACTIVOS[_TURNO][0])
                                    move_ganador(100, ganador)
                                    #ese jugador gana el juego
                                    print("Felicidades!")
                                    alerta = fuente1.render("Ha ganado la partida.", True,(0,0,0))
                                    screen.blit(alerta,[200,550])
                                    time.sleep(3.3)
                                    running = False

                                elif _JUGADORESACTIVOS[_TURNO][3] > 100:
                                #Ups, no cayo exacto. Retrocede las casillas debidas
                                    dif = _JUGADORESACTIVOS[_TURNO][3]-100
                                    _JUGADORESACTIVOS[_TURNO][3] = 100 - dif
                                    move_jugador(_JUGADORESACTIVOS[_TURNO])
                                    cas_interactiva, num = checkfor_casillainteractiva(_JUGADORESACTIVOS[_TURNO][3])
                                    if cas_interactiva:
                                        _JUGADORESACTIVOS[_TURNO][3] = num
                                        move_jugadoor(_JUGADORESACTIVOS[_TURNO])
                                    print(_JUGADORESACTIVOS[_TURNO])
                                    _TURNO = avanza_turno(_TURNO)

                            else:
                                _JUGADORESACTIVOS[_TURNO][3] += num_obtenido
                                if _JUGADORESACTIVOS[_TURNO][3] == 100:
                                    #ese jugador gana el juego
                                    print(_JUGADORESACTIVOS[_TURNO])
                                    place_jugador(100)
                                    print("Felicidades!")
                                    alerta = fuente1.render("Ha ganado la partida.", True,(0,0,0))
                                    screen.blit(alerta,[200,550])
                                    time.sleep(4)
                                    running = False
                                
                                elif _JUGADORESACTIVOS[_TURNO][3] > 100:
                                    #Ups, no cayo exacto. Retrocede las casillas debidas
                                    dif = _JUGADORESACTIVOS[_TURNO][3]-100
                                    _JUGADORESACTIVOS[_TURNO][3] = 100 - dif
                                    move_jugador(_JUGADORESACTIVOS[_TURNO])
                                    cas_interactiva, num = checkfor_casillainteractiva(_JUGADORESACTIVOS[_TURNO][3])
                                    if cas_interactiva:
                                        _JUGADORESACTIVOS[_TURNO][3] = num
                                        move_jugador(_JUGADORESACTIVOS[_TURNO])
                                        
                                    print(_JUGADORESACTIVOS[_TURNO])
                                    _TURNO = avanza_turno(_TURNO)

                                else:
                                    #avanza sin problema
                                    move_jugador(_JUGADORESACTIVOS[_TURNO])
                                    cas_interactiva, num = checkfor_casillainteractiva(_JUGADORESACTIVOS[_TURNO][3])
                                    if cas_interactiva:
                                        _JUGADORESACTIVOS[_TURNO][3] = num
                                        move_jugador(_JUGADORESACTIVOS[_TURNO])
                                        
                                    print(_JUGADORESACTIVOS[_TURNO])
                                    _TURNO = avanza_turno(_TURNO)
                            
                        else:
                            if num_obtenido != 5:
                                print("No es un 5. No puede avanzar")
                                alerta = fuente1.render("ALERTA,", True,(0,0,0))
                                screen.blit(alerta,[200,500])
                                alerta = fuente1.render("Debe lanzar un 5 para avanzar", True,(0,0,0))
                                screen.blit(alerta,[200,550])
                                _TURNO = avanza_turno(_TURNO)
                                
                            else:
                                _JUGADORESACTIVOS[_TURNO][2] = True
                    guardar_partida()
                                
        pygame.display.update()
        time.sleep(1.2)

    pygame.quit()
    quit()

main()
