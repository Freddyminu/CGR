from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint as rand

def Dados(raio, altura):
    altura /= 10

angulo_h = 400.0
angulo_v = 0
qualidade_renderi = 100
quantidade_chuva = 4000
chuva = []
raio = 0.90
largura  = 900
altura = 700

def keyboard(key,x,y):
    global angulo_h, angulo_v, qualidade_renderi

    key = ord(key)
    if key==27:
        exit(0)

def dist(Ponto):
    x = Ponto.xPos
    y = Ponto.yPos
    z = Ponto.zPos
    return (x*x+y*y+z*z)**(1/2)

class Chuva:
    def __init__(self):
        self.viva = True
        self.vida = 2
        self.desaparecer = rand(1,100) * 0.001 # DEFINO UM TEMPO PARA A CHUVA IR SUMINDO DO CHÃO
        self.xPos = rand(-1000,1000) / 1000
        self.yPos = 1.5
        self.zPos = rand(-1000,1000) /  1000
        self.vel = -rand(1,2) * 0.005
        self.gravidade = -0.000030
        self.ground = False 

def init():
    global chuva
    chuva = [Chuva() for i in range(quantidade_chuva)]

def snowRain():
    global chuva, raio
    glColor3f(0,127,255)
    for loop in range(0,quantidade_chuva,2):
        if dist(chuva[loop]) >= 3*raio: chuva[loop].viva = False        # VERIFICA SE ESTÁ DENTRO DO LUGAR DELIMITADO
        else: chuva[loop].viva = True
        if chuva[loop].viva:
            x = chuva[loop].xPos
            y = chuva[loop].yPos
            z = chuva[loop].zPos 
            glBegin(GL_LINES)
            glVertex3f(x, y, z)                                             # FAZ COM QUE CAIA EM UM CERTO GRAU
            glVertex3f(x, y + 0.03, z)                                      
            glEnd()
        if chuva[loop].yPos < -0.02: chuva[loop].ground = True            # DEFINE QUE ELE BATE NO " CHÃO", LUGAR DELIMITADO
        if not chuva[loop].ground: chuva[loop].yPos += chuva[loop].vel   # E SE NÃO COLIDIR, ELE INCREMENTA, PARA CAIR DENTRO DO LUGAR CERTO
        chuva[loop].vel += chuva[loop].gravidade
        chuva[loop].vida -= chuva[loop].desaparecer
        if (chuva[loop].vida < 0.0):
            chuva[loop] = Chuva()

def display():
    global angulo_h, angulo_v
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    snowRain() # AQUI EU ESTOU INSTANCIANDO A NEVE

    glClearColor(1.0/2,0.3/2,0.3/2,0.45) # DEFINE A COR DA JANELA ..
    glLoadIdentity()

    gluLookAt(4.2, 1.4, 0.0, 0.0, 0.4, 0.0, 0.0, 1.0, 0.0) # DEFINE COMO FICA A CAMERA
    
    glPushMatrix()
    
    glColor3f(0,127,255) # DEFINE A COR DA CHUVA
 
    glDisable(GL_BLEND)
    glPopMatrix()
    glFlush()
    glutSwapBuffers()

def reshape(w, h):
	glViewport(0, 0, w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(55, w / h, .1, 200)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(largura, altura)
glutCreateWindow("TC3_Chuva_FredericoMinuzzi_LucasEduardoFreitas")

init()
glutDisplayFunc(display)
glutIdleFunc(display)

glMatrixMode(GL_PROJECTION)
glViewport(0, 0, largura, altura)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
x = largura / altura
gluPerspective(45, x, .01, 100.0)
glMatrixMode(GL_MODELVIEW)
glShadeModel(GL_SMOOTH)
glClearDepth(1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
glClearColor(0.0, 0.0, 0.0, 1.0)

mat_shininess =  [ 15.0 ]                       # AQUI É FEITO O CONTROLE DE TEXTURA
mat_specular =    [ 0.75, 0.75, 0.75, 0.75 ]

light_ambient =  [   0.6, 0.6, 0.6, 1.0 ] # AQUI É FEITO O CONTROLE DE LUZ
light_position = [   6.0, 6.0, 2.0, 0.0 ]

glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular)
glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glLightfv(GL_LIGHT0, GL_POSITION, light_position)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
glutMainLoop()