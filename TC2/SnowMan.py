import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# variaveis
name = 'TC2_SnowMan_FredericoMinuzzi_LucasEduardoFreitas'
horizontal = 0
vertical = 0
Render = 200

def keyboard(key,x,y):
    global horizontal, vertical, Render
    
    print("vertical", vertical)
    print("horizontal", horizontal)
    print("Render", Render)
    
    #rotacionar o objeto todo em si...
    passo = 0.05
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

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    # Corpo
    glPushMatrix() # Atualiza o estado
     # Move o objeto
    glColor3f(1,1,1) # Cor do objeto
    glutSolidSphere(1.5,Render,Render) # Tipo de objeto em si
    glPopMatrix() 

    # Cabeca
    glPushMatrix() 
    glTranslatef(0,1.75,0)
    glColor3f(1,1,1)
    glutSolidSphere(1,Render,Render)
    glPopMatrix()

    # Chapeu baixo  
    glPushMatrix() 
    glTranslatef(0,2.60,0) 
    glRotatef(90,1,0,0) 
    glColor3f(0.1,0.1,0.1) 
    glutSolidCylinder(1.05,0.1,Render,Render) 
    glPopMatrix()

    # Chapeu topo  
    glPushMatrix()
    glTranslatef(0,3.50,0)
    glRotatef(90,1,0,0)
    glColor3f(0.1,0.1,0.1)
    glutSolidCylinder(0.6,1,Render,Render) 
    glPopMatrix()

    # Olho esquerdo
    glPushMatrix() 
    glTranslatef(0.90,2.05,0.30)
    glColor3f(0.1,0.1,0.1)
    glutSolidSphere(0.1,Render,Render)
    glPopMatrix()

    # Olho direito
    glPushMatrix() 
    glTranslatef(0.90,2.05,-0.30)
    glColor3f(0.1,0.1,0.1)
    glutSolidSphere(0.1,Render,Render)
    glPopMatrix()

    # Naris
    glPushMatrix()
    glTranslatef(0.95,1.75,0)
    glRotatef(90,0,1,0)
    glColor3f(1, 0.501960784, 0)
    glutSolidCone(0.1, 0.5, Render, Render)
    glPopMatrix()

    # Camisa
    glPushMatrix() 
    glTranslatef(0,0.05,0)
    glColor3f(0.5,0,0)
    glutSolidSphere(1.5,Render,Render)
    glPopMatrix()

    # Calca
    glPushMatrix() 
    glTranslatef(0,-0.05,0)
    glColor3f(0, 50/255, 20/255)
    glutSolidSphere(1.5,Render,Render)
    glPopMatrix()

    # Botao 1
    glPushMatrix() 
    glTranslatef(1.45+horizontal,0.3,0)
    glColor3f(0.1,0.1,0.1)
    glutSolidSphere(0.1,Render,Render)
    glPopMatrix()

    # Botao 2
    glPushMatrix() 
    glTranslatef(1.275,0.3+0.5,0)
    glColor3f(0.1,0.1,0.1)
    glutSolidSphere(0.1,Render,Render)
    glPopMatrix()

    glutSwapBuffers()
    return
    
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) #inicializa o tipo de modo de display
    glutInitWindowSize(800,1000) #da o tamanho da janela
    glutCreateWindow(name) # cira a janela e coloca oq ta ali como titulo
    glClearColor(1.0/2,0.3/2,0.3/2,0.45) # faz  a cor da janela
    glShadeModel(GL_SMOOTH) # indica um estilo de shading..

    glutDisplayFunc(display) # func de chamada pra tela
    glutKeyboardFunc(keyboard) #input
    glutIdleFunc(display) #atualiza a tela, sem isso o teclado nao funciona por exemplo, seu burro

    glEnable(GL_CULL_FACE) #
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

    lightPosition = [ 10, 4, 10, 1] # posicao da luz
    lightColor = [ 0.4, 0.4, 0.4, 1.0] # cor da luz
    
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition) # cria uma luz 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.01)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    
    glEnable(GL_LIGHT0)
    

    glMatrixMode(GL_PROJECTION) # specifica qual matrix eh o target
    gluPerspective(40,0.6,6,80)   
    glMatrixMode(GL_PROJECTION)

    # glMatrixMode(GL_MODELVIEW)

    gluLookAt(18,3,20/-4,
              0,0,0,
              0,1,0)

    glPushMatrix()
    glutMainLoop()