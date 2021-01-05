import coin
import map
import extra
import ghost
import pacman
import readfromoutside
from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

'''
https://pixabay.com/illustrations/start-start-black-button-button-web-1436754/
https://pixabay.com/illustrations/winner-success-success-concept-1182937/
https://pixabay.com/photos/nature-sky-night-stars-2609647/
https://pixabay.com/photos/game-over-game-over-computer-2720584/
https://pixabay.com/photos/wood-floor-backdrop-background-1866667/
'''
import sys

maze = [[0 for x in range(20)] for y in range(20)]  # 2D array maze tutma

pacman_call = pacman.Pacman()
ghost_call = ghost.Ghost()
Extra_call = extra.Extra()

start = 0  # başlama ekranı
one = 1  # starta sadece bir kez kullanması
pacman_column = 7  # Pacman y konumu tutma
pacman_line = 7  # Pacman x konumu tutma
ghost_column = 4  # Ghost1 y konumu tutma
ghost_line = 1  # Ghost1 x konumu tutma
ghost_column1 = 10  # Ghost2 y konumu tutma
ghost_line1 = 13  # Ghost2 x konumu tutma
ghost_line2 = 13  # Ghost3 x konumu tutma
ghost_column2 = 4  # Ghost3 y konumu tutma
soul = 0  # Pacman hayati
level = 1  # hangi level de olduğumu belirliyor
Call_coin = coin.Coin(level)


class Main:
    def __init__(self, leveln):
        global level, pacman_column, pacman_line, pacman_call
        level = leveln

    # maze çizim fonksiyonlari çağriliyor
    def draw(self):
        global start, Extra_call, maze, pacman_column, pacman_line
        global ghost_column, ghost_line, ghost_column1, ghost_line1, ghost_line2, ghost_column2
        global pacman_call, ghost_call, Call_coin, level
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1.0, 20.0, -1.0, 15.0, 0, 10)
        glPushMatrix()
        glActiveTexture(GL_TEXTURE0)
        add_image = readfromoutside.Readfromoutside()
        add_image.LoadTexture("tre2.jpg", 1)
        add_image.LoadTexture("floor3.jpg", 2)
        add_image.LoadTexture("gameoverl.jpg", 13)
        add_image.LoadTexture("start.jpg", 14)
        add_image.LoadTexture("ghost.jpg", 7)
        add_image.LoadTexture("winne.jpg", 15)
        add_image.LoadTexture("ghost3.jpeg", 20)
        add_image.LoadTexture("ghost1.jpeg", 8)
        add_image.LoadTexture("ghost2.jpeg", 9)
        glEnable(GL_TEXTURE_2D)
        glPopMatrix()
        Read_text = readfromoutside.Readfromoutside()
        Draw_maze = map.Map()
        if start == 0:
            glPushMatrix()
            Extra_call.startgame()
            glPopMatrix()
        else:
            if level > 0:
                glPushMatrix()
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                gluLookAt(0.0, -1.0, 8.0, -2.0, 0.0, 4.0, -9.0, 156.0, 17.0)
                maze = Read_text.readObj("maze" + str(level) + ".txt")
                # coin çizme
                glPushMatrix()
                Call_coin.drawcoin(level)
                glPopMatrix()
                # maze çizme
                glPushMatrix()
                Draw_maze.drawmaze(maze)
                glPopMatrix()
                # ghostlar çizme
                glPushMatrix()
                ghost_call.draw_ghost(ghost_column, ghost_line, 1, maze)
                ghost_call.draw_ghost(ghost_column2, ghost_line2, 3, maze)
                ghost_call.draw_ghost(ghost_column1, ghost_line1, 2, maze)
                glPopMatrix()
                # pacman çizme
                glPushMatrix()
                pacman_call.drawpacman(pacman_column, pacman_line, maze)
                glPopMatrix()

                glPushMatrix()
                ghost_move()
                glPopMatrix()

                glPopMatrix()
                if Call_coin.score() == level:
                    level += 1
        # ouyn bitti zaman bu if çalışıyor
        if level < 0:
            glPushMatrix()
            Extra_call.gameover()
            glPopMatrix()
        # ouyna kazandin zaman bu if çalışıyor
        if level == 5:
            glPushMatrix()
            Extra_call.win()
            glPopMatrix()
        glFlush()

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)

    # oyun ilk çalıştığı zaman bir kez çalıcak start ekranıden geçme
    def keyPressed(self, *args):
        if (args[2] > 0 or args[2] < 0):
            global one, start
            if (one == 1):
                start += 1
                one -= 1
        glFlush()

    # pacman ok tuşları ile hareket etmesi için ve ayni zaman hangi
    # coın yediğini Call_coin.delete ile kaydedecek
    def ok_key(self, key, x, y):
        global pacman_column, pacman_line, ghost_column, ghost_line
        global pacman_call, ghost_call, Call_coin

        if key == GLUT_KEY_RIGHT:
            if 1 == pacman_call.move(4):
                pacman_line += 1
                Call_coin.delete(pacman_column, pacman_line)
        elif key == GLUT_KEY_LEFT:
            if 1 == pacman_call.move(3):
                pacman_line -= 1
                Call_coin.delete(pacman_column, pacman_line)
        elif key == GLUT_KEY_UP:
            if 1 == pacman_call.move(1):
                pacman_column -= 1
                Call_coin.delete(pacman_column, pacman_line)
        elif key == GLUT_KEY_DOWN:
            if 1 == pacman_call.move(2):
                pacman_column += 1
                Call_coin.delete(pacman_column, pacman_line)
        glutPostRedisplay()
    # oyundaki tüm ghost'ler nasil hareket edecekler belirliyor ve sonraki adim duvar var mi yok mi da biliyor
    # ghostlar çalışma şekli random olarak harket ediyor ve 5 kez yaşma şansı var ondan sonra oyun bitter


def ghost_move():
    global pacman_column, pacman_line, ghost_column, \
        ghost_line, ghost_column1, ghost_line1, ghost_line2, ghost_column2
    global maze, soul, level
    # birinci ghost random harketi oluşturma
    random_number = random.randint(1, 4)
    if random_number == 1 and maze[ghost_column][ghost_line + 1] == 0:
        ghost_line += 1
    elif random_number == 2 and maze[ghost_column - 1][ghost_line] == 0:
        ghost_column -= 1
    elif random_number == 3 and maze[ghost_column][ghost_line - 1] == 0:
        ghost_line -= 1
    elif random_number == 4 and maze[ghost_column + 1][ghost_line] == 0:
        ghost_column += 1
    # ikinci ghost random harketi oluşturma
    random_number1 = random.randint(1, 4)
    if random_number1 == 4 and maze[ghost_column1][ghost_line1 + 1] == 0:
        ghost_line1 += 1
    elif random_number1 == 3 and maze[ghost_column1 - 1][ghost_line1] == 0:
        ghost_column1 -= 1
    elif random_number1 == 2 and maze[ghost_column1][ghost_line1 - 1] == 0:
        ghost_line1 -= 1
    elif random_number1 == 1 and maze[ghost_column1 + 1][ghost_line1] == 0:
        ghost_column1 += 1
    # üçüncü ghost random harketi oluşturma
    random_number2 = random.randint(1, 4)
    if random_number2 == 4 and maze[ghost_column2][ghost_line2 + 1] == 0:
        ghost_line2 += 1
    elif random_number2 == 3 and maze[ghost_column2 - 1][ghost_line2] == 0:
        ghost_column2 -= 1
    elif random_number2 == 2 and maze[ghost_column2][ghost_line2 - 1] == 0:
        ghost_line2 -= 1
    elif random_number2 == 1 and maze[ghost_column2 + 1][ghost_line2] == 0:
        ghost_column2 += 1
    # her hangi ghost ile pacman ayni x ve y kordinatta olduğuzaman bir hayat kayıp ediyor.
    if (pacman_column == ghost_column) and\
            (ghost_line == pacman_line) or (pacman_column == ghost_column1) and (
            ghost_line1 == pacman_line) or (pacman_column == ghost_column2) and (ghost_line2 == pacman_line):
        soul += 1
        if soul > 5:
            level = -1
    # dört levelden oluşuyor her level bitti zaman sonraki levele geçiyor


def main():
    global level
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"PACMAN GAME NEW UPDATE")
    if level == 1:
        start_game = Main(1)
    if level == 2:
        start_game = Main(2)
    if level == 3:
        start_game = Main(3)
    if level == 4:
        start_game = Main(4)
    glutDisplayFunc(start_game.draw)
    glutIdleFunc(start_game.draw)
    glutMouseFunc(start_game.keyPressed)
    glutSpecialFunc(start_game.ok_key)
    start_game.InitGL()
    glutMainLoop()


main()
