from OpenGL.GL import *
from OpenGL.GL import glBegin

from OpenGL.GLUT import *
from array import *
from OpenGL.GLU import *
from PIL import Image
import random

import sys
maze = [[0 for x in range(20)] for y in range(20)]#2D array
ghost_column = 0 #ghost y kordinati
ghost_line = 0 #ghost x kordinati
hight = 0 # y kordinati
width = 0 # x kordinati


class Ghost :
    #mazedeki ghostlar çiziyor
    def draw_ghost(self, column , line , Number, mazes=[[0 for x in range(20)] for y in range(20)]):
        global maze, ghost_column, ghost_line
        global hight , width
        for i in range(15):
            for n in range(15):
                maze[i][n] = mazes[i][n]
        ghost_column = column
        ghost_line = line
        hight = 15 - column
        width = line + 1
        glPushMatrix()

        if Number == 1 :
            glBindTexture(GL_TEXTURE_2D,8)
        if Number == 2 :
            glBindTexture(GL_TEXTURE_2D,9)
        if Number == 3 :
            glBindTexture(GL_TEXTURE_2D,20)
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glTexCoord2f(0, 1)
        glVertex3f(width - 1, hight, 1)
        glTexCoord2f(0, 0)
        glVertex3f(width, hight, 1)
        glTexCoord2f(1, 0)
        glVertex3f(width, hight - 1, 1)
        glTexCoord2f(1, 1)
        glVertex3f(width - 1, hight - 1, 1)

        glColor3f(1, 1, 1)
        glTexCoord2f(0, 1)
        glVertex3f(width - 1, hight, 1)
        glTexCoord2f(0, 0)
        glVertex3f(width, hight, 1)
        glTexCoord2f(1, 0)
        glVertex3f(width, hight, 0)
        glTexCoord2f(1, 1)
        glVertex3f(width - 1, hight, 0)

        glColor3f(1, 1, 1)
        glTexCoord2f(0, 1)
        glVertex3f(width, hight, 1)
        glTexCoord2f(0, 0)
        glVertex3f(width, hight - 1, 1)
        glTexCoord2f(1, 0)
        glVertex3f(width, hight - 1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(width, hight, 0)

        glColor3f(1, 1, 1)
        glTexCoord2f(0, 1)
        glVertex3f(width, hight - 1, 1)
        glTexCoord2f(0, 0)
        glVertex3f(width - 1, hight - 1, 1)
        glTexCoord2f(1, 0)
        glVertex3f(width - 1, hight - 1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(width, hight - 1, 0)

        glColor3f(1, 1, 1)
        glTexCoord2f(0, 1)
        glVertex3f(width - 1, hight - 1, 1)
        glTexCoord2f(0, 0)
        glVertex3f(width - 1, hight, 1)
        glTexCoord2f(1, 0)
        glVertex3f(width - 1, hight, 0)
        glTexCoord2f(1, 1)
        glVertex3f(width - 1, hight - 1, 0)

        glColor3f(1, 1, 1)
        glTexCoord2f(0, 1)
        glVertex3f(width - 1, hight, 0)
        glTexCoord2f(0, 0)
        glVertex3f(width, hight, 0)
        glTexCoord2f(1, 0)
        glVertex3f(width, hight - 1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(width - 1, hight - 1, 0)
        glEnd()
        glPopMatrix()
