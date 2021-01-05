from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from array import *
from OpenGL.GLU import *
from PIL import Image

import sys

class Extra:
    # start game ekrani çiziyor
    def startgame(self):
        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, 14)
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glTexCoord2f(1, 0)
        glVertex3f(20, 15, 0)
        glTexCoord2f(0, 0)
        glVertex3f(-1, 15, 0)
        glTexCoord2f(0, 1)
        glVertex3f(-1, -1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(20, -1, 0)
        glEnd()
        glPopMatrix()
    # oyun bitti ekrani çiziyor
    def gameover(self):
        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, 13)
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glTexCoord2f(1, 0)
        glVertex3f(20, 15, 0)
        glTexCoord2f(0, 0)
        glVertex3f(-1, 15, 0)
        glTexCoord2f(0, 1)
        glVertex3f(-1, -1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(20, -1, 0)
        glEnd()
        glPopMatrix()
    # win ekrani çiziyor
    def win(self):
        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, 15)
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glTexCoord2f(1, 0)
        glVertex3f(20, 15, 0)
        glTexCoord2f(0, 0)
        glVertex3f(-1, 15, 0)
        glTexCoord2f(0, 1)
        glVertex3f(-1, -1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(20, -1, 0)
        glEnd()
        glPopMatrix()




