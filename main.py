from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
#2.Ders uygulamasi
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def plotfuc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)

    #x koordinat sistemi
    glBegin(GL_LINES)
    glVertex2f(-5.0,0.0)
    glVertex2f(5.0,0.0)
    glEnd()

    #y koordinat sistemi
    glBegin(GL_LINES)
    glVertex2f(0.0,-5.0)
    glVertex2f(0.0,5.0)
    glEnd()

    glPointSize(3.0)
    for x in arange(-10.0, 10.0, 0.05):
        #y = sin(x)
        y=cos(x)
        #y=2*x*x-2
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Plot Points")
    glutDisplayFunc(plotfuc)
    init()
    glutMainLoop()

main()
