import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# variaveis
name = 'TC5_Textura_FredericoMinuzzi_LucasEduardoFreitas'
horizontal = 0
vertical = 0
Render = 25

def keyboard(key,x,y):

    global horizontal, vertical, Render
    
    print("vertical", vertical)
    print("horizontal", horizontal)
    print("Render", Render)
    
    #rotacionar o objeto todo em si...
    passo = 2
    passoint = 1
    rotacionarobjeto = 5

    if vertical <= -52:
        vertical = -51

    if vertical >= 52:
        vertical = 51
        
    
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
 

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
   

    glPopMatrix()
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
    


    gluLookAt(0,10,60,
              0,0,0,
              0,60,10)

    glPushMatrix()
    glutMainLoop()