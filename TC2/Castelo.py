import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# variaveis
name = 'TC2_Castelo_FredericoMinuzzi_LucasEduardoFreitas'
horizontal = 0
vertical = 0
Render = 200

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

    # estes sao para colocacao de objetos   
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

    # reset
    elif key == b'r':
        angulo_h = 300.0
        angulo_v = 0
        horizontal = 1
        vertical = 0  

def torreCyclindrica(PosX,PosY,PosZ):
    glPushMatrix() 
    glRotatef(270,1,0,0) 
    glTranslate(PosX,PosY,PosZ)
    glColor3f(0.5,0,0)
    glutSolidCylinder(0.90,5.40,Render,Render) 
    glTranslate(0,0,5.40)
    glColor3f(0, 50/255, 20/255)
    glutSolidCone(1.3, 2.80, Render, Render)
    #neve
    glTranslate(0,0,0.5)
    glColor3f(0.8, 0.8, 0.8)
    glutSolidCone(1.3, 4, Render, Render)   
    glPopMatrix()
    return
def paredeInteira(PosX,PosY,PosZ, Angulo,RotX,RotY,RotZ):
    glPushMatrix()
    glRotate(Angulo,RotY,RotX,RotZ) 
    glTranslate(PosX, PosY, PosZ)
    glColor3f(0, 50/255, 20/255)
    glScaled(0.25,1,6)
    glutSolidCube(3.24)
    #neve
    glTranslated(0,3.24-1.5,0)
    glScaled(1,0.1,1)
    glColor3f(0.8,0.8,0.8)
    glutSolidCube(3.24)
    glPopMatrix()
    return

def paredeMetade(PosX, PosY,PosZ):
    glPushMatrix()
    glRotate(90,0,1,0) 
    glTranslate(PosX,PosY,PosZ)
    glColor3f(0, 50/255, 20/255)
    glScaled(0.25,1,2.5)
    glutSolidCube(3.24)
    #neve
    glTranslated(0,3.24-1.5,0)
    glScaled(1,0.1,1)
    glColor3f(0.8,0.8,0.8)
    glutSolidCube(3.24)
    glPopMatrix()
    return
def Grama():
    # Grama
    glPushMatrix() 
    glRotatef(90,1,0,0) 
    glColor3f(128/255, 1, 100/255)
    glTranslated(0,0,0.02)
    glRectf(-200,200,200,-200); # Retangulo 2d com cordenadas
    glRotatef(180,1,0,0) 
    glTranslated(0,0,-0.01)
    glRectf(-80,80,80,-80); 
    glPopMatrix()
    return
def ChaoDoCastelo():
    # Chão Olhando de baixo e cima.
    glPushMatrix() 
    glColor3f(0.8,0.8,0.8)	
    glRotatef(90,1,0,0) 
    glRectf(-10,10,10,-10); # Retangulo 2d com cordenadas
    glPopMatrix()
def Torrecentral():
    glPushMatrix() 
    glColor3f(0.5,0,0)
    glRotatef(270,1,0,0) 
    glScaled(0.5,0.5,2)
    glTranslate(0,0,3.5)
    glutSolidCube(7)
    #neve
    glTranslated(0,0,7-3.4000000000000017)
    glScaled(1,1,0.032)
    glColor3f(0.8,0.8,0.8)
    glutSolidCube(7)
    glPopMatrix()
    return
def Entrada():
    # Entrada Frontal
    glPushMatrix()
    glTranslated(0,1.62,10+1.62-0.41)
    glScaled(0.80,1,1)
    glColor3f(0, 50/255, 20/255)
    glutSolidCube(3.24)
    #neve
    glTranslated(0,3.24-1.5,0)
    glScaled(1,0.1,1)
    glColor3f(0.8,0.8,0.8)
    glutSolidCube(3.24)
    glPopMatrix()
    return  
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    torreCyclindrica(-10,10,0) #Torre Esquerda Fundo
    torreCyclindrica(10,-10,0) #Torre Direita Frontal
    torreCyclindrica(-10,-10,0) #Torre Esquerda Frontal 
    torreCyclindrica(10,10,0) #Torre Direita Fundo
    
    paredeInteira(-10,1.64,0, 0,0,0,0) # Parede da Esquerda
    paredeInteira(+10,1.64,0, 0,0,0,0) # Parede da direita
    paredeInteira(+10,1.64,0, 90,1,0,0) # Parede do Fundo

    paredeMetade(-10,1.64,5.3) # Parede Frontal Direita
    paredeMetade(-10,1.64,-5.3) # Parede Frontal Esquerda
    
    Grama()
    ChaoDoCastelo()
    Torrecentral()
    Entrada()
    
    glutSwapBuffers()
    return
    
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) #inicializa o tipo de modo de display
    glutInitWindowSize(1000,1000) #da o tamanho da janela
    glutCreateWindow(name) # cira a janela e coloca oq ta ali como titulo
    glClearColor(153/255, 204/255, 1,0.6) # faz  a cor da janela
    glShadeModel(GL_SMOOTH) # indica um estilo de shading..

    #glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE) # deixando tudo preto...................................

    glutDisplayFunc(display) # func de chamada pra tela
    glutKeyboardFunc(keyboard) #input
    glutIdleFunc(display) #atualiza a tela, sem isso o teclado nao funciona por exemplo, seu burro

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

    lightPosition = [ -10, -10, 10, 1] # posicao da luz
    lightColor = [ 0.4, 0.4, 0.4, 1.0] # cor da luz
    
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition) # cria uma luz 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.01)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    
    glEnable(GL_LIGHT0)
    
    glMatrixMode(GL_PROJECTION) # specifica qual matrix eh o target
    gluPerspective(55,0.6,6,200)   
    glMatrixMode(GL_PROJECTION)

    # glMatrixMode(GL_MODELVIEW)

    gluLookAt(0,20,60,
              0,0,0,
              0,60,10)

    glPushMatrix()
    glutMainLoop()
    
  



