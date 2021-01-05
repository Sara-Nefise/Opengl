from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from array import *
from OpenGL.GLU import *
from PIL import Image
import readfromoutside

import sys
maze = [[0 for x in range(20)] for y in range(20)]# 2D array maze tutma
hight1 = 0 #y kordinati
width1 = 0 #x kordinati
deneme = 1
il = [1500] # pacman yediği coin x kordinati
nl = [1500] # pacman yediği coin y kordinati
first = 0 # sonraki level geçtiğimiz zaman ilde ve nlde başladi eleman
m = 0 # il ve nl capacity
i_n = -1#x kordinati
i_s = -1#y kordinati
score = 0 # genel score
score1 = 0 # birinci score
score2 = 0 # ikinci score
score3 = 0 # üçüncü score
score4 = 0 # dörtüncü score

class Coin :
    #dışardan mazeler txt dosyasından alıyor
    def __init__(self , level):
        global maze
        Read_text = readfromoutside.Readfromoutside()
        if level == 1:
            maze = Read_text.readObj("maze1.txt")
        if level == 2:
            maze = Read_text.readObj("maze2.txt")
        if level == 3:
            maze = Read_text.readObj("maze3.txt")
        if level == 4:
            maze = Read_text.readObj("maze4.txt")
    # mazedeki coin çiziyor
    def drawcoin(self,level):
        global hight1, width1 , maze , deneme , il , nl , m , i_s , i_n
        global score,score1, score2, score3, score4 , first
        for i in range(15):
            for n in range(15):
                glPushMatrix()
                # pacman yediği coin buluyor
                for s in range(first , m):
                    if (il[s]==i) and (nl[s]==n):
                        i_s = i
                        i_n = n
                # pacman yediği coin -3 z kordinata indiriyor.
                if ((i==i_s) and (n==i_n) and (deneme>0)):
                    glTranslate(0, 0, -3)
                    score += 1
                #coin çiziyor
                if 0 == maze[i][n]:
                    glColor3f(0.60, 0.54, 0.0)
                    width1 = n + 0.5
                    hight1 = 15 - i - 0.5
                    glTranslate(width1, hight1, 1)
                    glutSolidSphere(0.1, 20, 20)
                glPopMatrix()
        # score level göre veriyor.
        if level == 1:
            score1 = score
        if level == 2:
            score2 = score
        if level == 3:
            score3 = score
        if level == 4:
            score4 = score
        score = 0
    # pacman geçti x ve y kordinattan coin varsa onu kaydedecek
    def delete(self,pacman_column,pacman_line ):
        global maze, deneme,  il, nl, m,score ,score1, score2, score3, score4
        if maze[pacman_column][pacman_line] == 0:
            il.append(pacman_column)
            nl.append(pacman_line)
            m += 1
            deneme += 1
        return 0
    #tüm mazedeki coin yedikten sora sonraki levele geçme
    def score(self):
        global score,score1, score2, score3, score4 , m , il ,nl,first
        if score1 == 116:
            score = 0
            first = m
            score1 = 0
            return 1
        if score2 == 105:
            first = m
            score = 0
            score2 = 0
            return 2
        if score3 == 114:
            score = 0
            first = m
            score3 = 0
            return 3
        if score4 == 106:
            score = 0
            first = m
            score4 = 0
            return 4
        return 0