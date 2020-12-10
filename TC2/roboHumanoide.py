import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# variaveis
name = 'TC2_roboHumanoide_FredericoMinuzzi_LucasEduardoFreitas'
horizontal = 0
vertical = 0
Render = 25

def keyboard(key,x,y):

    global horizontal, vertical, Render
    
    print("vertical", vertical)
    print("horizontal", horizontal)
    print("Render", Render)
    
    #rotacionar o objeto todo em si...
    passo = 0.1
    passoint = 1
    rotacionarobjeto = 5
    
    if key == b'w':
        glRotate(rotacionarobjeto, 1,0,0) 
    elif key == b's':
        glRotate(rotacionarobjeto, -1,0,0) 
    elif key == b'd':
        glRotate(rotacionarobjeto, 0,1,0) 
    elif key == b'a':
        glRotate(rotacionarobjeto, 0,-1,0) 

    # estes sao para colocacao de objetos, ajudaram MUITO  
    elif key == b'u':
        vertical += passo
    elif key == b'j':
        vertical -= passo
    elif key == b'k':
        horizontal += passo
    elif key == b'h':
        horizontal -= passo
    
    # Render de rederizacao
    elif key == b'+':
        Render += passoint
    elif key == b'-':
        Render -= passoint
 
def Tronco():
    glPushMatrix() 
    glColor3f(1, 159/255, 100/255)
    glScaled(1,3,1) #x z y 
    glutSolidCube(2)
    glPopMatrix()
    return

def cabeca():
    glPushMatrix() 
    glColor3f(1, 159/255, 100/255)
    glScaled(1,1,1) #x z y 
    glTranslate(0,4.25,0) #x z y 0.5 de espaco do corpo
    glutSolidCube(1.75)
    glPopMatrix()
    return

def pe(posX,posZ,posY):
    glPushMatrix() 
    glColor3f(1, 159/255, 100/255)
    glTranslate(posX,posZ,posY) #x z y 
    glScaled(0.60,0.35,1.5) #x z y 
    glutSolidCube(1)
    glPopMatrix()
    return

def Articulacao(posX,posZ,posY): #ladoDoCorpo (-1 esquerda, 1 Direita)
    glPushMatrix() 
    glColor3f(0.5,0,0)
    glRotated(90,0,1,0)
    glScaled(0.5,0.5,0.5) # x z y 
    glTranslate(posX,posZ,posY) #x z y 
    glutSolidCylinder(1, 1, Render, Render)
    glPopMatrix()
    return

def limb(posX,posZ,posY):
    glPushMatrix() 
    glColor3f(0, 70/255, 50/255)
    glScaled(0.45,2,0.75) # x y z
    glTranslate(posX,posZ,posY) #x y z 
    glutSolidCube(1)
    glPopMatrix()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    Tronco()
    cabeca() 

    Articulacao(0,6,-0.5) #Pescoso

    Articulacao(0,5,2)#socket shoulder Direito
    Articulacao(0,0.9,2) #socket braco-antebraco Direito
    Articulacao(0,5,-3) #socket shoulder Esquerdo
    Articulacao(0,0.9,-3) #socket braco-antebraco Esquerdo
    limb(-2.75,0.75,0)  #Braco Esquerdo
    limb(+2.75,0.75,0)  #Braco Direito
    limb(-2.75,-0.4,0)  #Antebraco Esquerdo
    limb(+2.75,-0.4,0)  #Antebraco Direito

    Articulacao(0,-6,0.55)#socket bacia Direto
    Articulacao(0,-10.5,0.55)#socket Coxa-Perna Direto
    Articulacao(0,-6,-1.55)#socket bacia Esquerdo
    Articulacao(0,-10.5,-1.55)#socket Coxa-Perna Esquerdo
    limb(+1.16,-2.1,0) #Coxa Direita
    limb(-1.16,-2.1,0) #Coxa Esquerda
    limb(+1.16,-3.2,0) #Perna Direita
    limb(-1.16,-3.2,0) #Perna Esquerda

    Articulacao(0,-14.5,0.55)#socket Perna-pe Direto
    Articulacao(0,-14.5,-1.55)#socket Perna-pe Esquerdo
    pe(0.535,-7.575,0.55) #pe esquerdo
    pe(-0.535,-7.575,0.55) #pe direito
    
    
    glutSwapBuffers()
    return
    
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) #inicializa o tipo de modo de display
    glutInitWindowSize(670,900) #da o tamanho da janela
    glutCreateWindow(name) # cira a janela e coloca oq ta ali como titulo
    glClearColor(153/255, 204/255, 1,0.6) # faz  a cor da janela
    glShadeModel(GL_SMOOTH) # indica um estilo de shading..

    glutDisplayFunc(display) # func de chamada pra tela
    glutKeyboardFunc(keyboard) #input
    glutIdleFunc(display) #atualiza a tela, sem isso o teclado nao funciona por exemplo, seu burro
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

    lightColor = [ 0.7, 0.7, 0.7, 1.0] # cor da luz

    lightPosition = [ -10, 10, 10, 1] # posicao da luz0
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition) # cria uma luz0 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.01)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    
    lightPosition2 = [ 50, -15, 15, 1] # posicao da luz1
    glLightfv(GL_LIGHT1, GL_POSITION, lightPosition2) # cria uma luz1 
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightColor)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.01)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)
    
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glMatrixMode(GL_PROJECTION) # specifica qual matrix eh o target
    gluPerspective(16.5,0.6,6,200)  #FOV  e os maximo e minimos dos planos (Clipping)
    glMatrixMode(GL_PROJECTION)


    gluLookAt(0,10,60,
              0,0,0,
              0,60,10)

    glPushMatrix()
    glutMainLoop()
    
  



