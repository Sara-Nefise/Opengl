from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from array import *
from OpenGL.GLU import *
from PIL import Image

import sys

maze = [[0 for x in range(20)] for y in range(20)]#2D array
pacmanline = 0 # pacman x kordinati
pacmancolumn = 0# pacman y kordinati
hight = 0#y kordinati
width = 0#x kordinati
class Pacman:
    #pacman çiziyor
    def drawpacman(self, column, line, mazes=None):
        if mazes is None:
            mazes = [[0 for x in range(20)] for y in range(20)]
        global maze  ,pacmancolumn, pacmanline , hight , width
        for i in range(15):
            for n in range(15):
                maze[i][n] = mazes[i][n]
        glPushMatrix()
        pacmancolumn = column
        pacmanline = line
        hight = 15 - column - 0.5
        width = line + 1 + 0.5
        glTranslate(width -1 , hight, 1)
        glColor3f(0.55, 0.54, 0.0)
        glutSolidSphere(0.5, 20, 20)
        glPopMatrix()
    #pacman hareket etti zaman kontrol ediyor duvar varsa ve konumu x ve y krodinatta değiştiriyor
    def move(self , place):
        global maze, pacmancolumn, pacmanline
        global up , down , left , right
        if (place == 1) and maze[pacmancolumn - 1][pacmanline] == 0 :
            pacmancolumn -= 1
            return 1
        elif (place == 2) and maze[pacmancolumn + 1][pacmanline] == 0:
            pacmancolumn += 1
            return 1
        elif (place == 3) and maze[pacmancolumn][pacmanline - 1] == 0:
            pacmanline -= 1
            return 1
        elif (place == 4) and maze[pacmancolumn][pacmanline + 1] == 0:
            pacmanline += 1
            return 1
        return 0
