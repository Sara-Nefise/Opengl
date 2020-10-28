from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def mavi():
    glColor3f(0.0, 0.999, 0.999)

def siyah():
    glColor3f(0, 0, 0.0)

def koyu_pembe():
    glColor3f(0.5, 0.0, 0.0)

def yesil():
    glColor3f(0.0, 1.0, 0.0)

def kirmizi():
    glColor3f(1.0, 0.0, 0.0)



def kenarekleme():
    siyah()
    glLineWidth(3)
    posx, posy = -2.01, -2.51
    sides = 32
    radius = 0.5
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

    glLineWidth(3)
    posx, posy = +2.01, -2.51
    sides = 32
    radius = 0.5
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()
    glFlush()



def keyPressed(*args):
    print(args[0])
    if args[0] == bytes('Esc'):
        sys.exit()
    elif args[0] == bytes('g', 'utf-8') or args[0] == bytes('b', 'utf-8') or args[0] == bytes('r', 'utf-8'):

        if args[0] == bytes('r', 'utf-8'):
            plotTerrain('r') #kirmizi

        elif args[0] == bytes('g', 'utf-8'):
            plotTerrain('g') #  color(yesil)

        elif args[0] == bytes('b', 'utf-8'):
            plotTerrain('b') # color(mavi)
    glutPostRedisplay()


def plotTerrain(reng=''):
    glClear(GL_COLOR_BUFFER_BIT)
    if(reng=='r'):
        kirmizi()
    elif(reng=='g'):
        yesil()
    elif(reng=='b' or reng==''):
        mavi()

    glBegin(GL_QUADS)
    glVertex2f(-2, 0)
    glVertex2f(+2, 0)
    glVertex2f(+2, +1.5)
    glVertex2f(-2, +1.5)
    if (reng == 'r'):
        kirmizi()
    elif (reng == 'g'):
        yesil()
    elif (reng == 'b'):
        mavi()
    elif(reng==''):
        koyu_pembe()
    glVertex2f(-3.5, 0)
    glVertex2f(+3.5, 0)
    glVertex2f(+3.5, -2)
    glVertex2f(-3.5, -2)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    if (reng == 'r'):
        kirmizi()
    elif (reng == 'g'):
        yesil()
    elif (reng == 'b'):
        mavi()
    elif (reng == ''):
        siyah()
    glVertex2f(-2.01, 0.01)
    glVertex2f(+2.01, 0.01)
    glVertex2f(+2.01, +1.51)
    glVertex2f(-2.01, +1.51)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-3.51, 0.01)
    glVertex2f(+3.51, 0.01)
    glVertex2f(+3.51, -2.01)
    glVertex2f(-3.51, -2.01)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 0.0)
    glVertex2f(+0, -2.0)
    glEnd()
    if (reng == 'r'):
        kirmizi()
    elif (reng == 'g'):
        yesil()
    elif (reng == 'b'):
        mavi()
    elif (reng == ''):
        siyah()
    posx, posy = -2, -2.5
    sides = 32
    radius = 0.5
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

    posx, posy = +2, -2.5
    sides = 32
    radius = 0.5
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)

    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Plot Points")
    glutDisplayFunc(plotTerrain)
    glutKeyboardFunc(keyPressed)







    init()

    glutMainLoop()


main()