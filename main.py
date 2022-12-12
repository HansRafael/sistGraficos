import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from draw_morrinho import DrawMorrinho
from draw_furg_logo import DrawFURGLogo
from draw_floor import DrawFloor
import sys
import lights as lg
import numpy as np
import operations as opMatrix

def main():
    pygame.init()
    display = (1200, 700)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Arthur, Hans e Laura projetao - FURG')
    
    # Enable showing in the front
    glEnable(GL_DEPTH_TEST)

    # Lights
    lg.lights()
    
    # Projection and perpective
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    print(f'initial {viewMatrix}')
    glLoadIdentity()

    # Init mouse movement and center mouse on screen
    displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)

    up_down_angle = 0.0
    paused = False
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                    paused = not paused
                    pygame.mouse.set_pos(displayCenter) 
            if not paused: 
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pygame.mouse.set_pos(displayCenter)    

        if not paused:
            # Get keys
            keypress = pygame.key.get_pressed()
                    
            # Init model view matrix
            glLoadIdentity()

            # Apply the look up and down
            up_down_angle += mouseMove[1]*0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            # Init the view matrix
            glPushMatrix()
            glLoadIdentity()

            #apply rotate movent
            if keypress[pygame.K_x]:
                matrixRotate = opMatrix.glsRotateX(0.1)
                glMultMatrixf(matrixRotate)
            if keypress[pygame.K_y]:
                matrixRotate = opMatrix.glsRotateY(0.1)
                glMultMatrixf(matrixRotate)
            if keypress[pygame.K_z]:
                matrixRotate = opMatrix.glsRotateZ(0.1)
                glMultMatrixf(matrixRotate)
      
            
            # Apply the movement translate
            if keypress[pygame.K_w]:
                matrixTranslate = opMatrix.glTranslatef(0,0,0.1)
                glMultMatrixf(matrixTranslate)
            
            if keypress[pygame.K_s]:
                matrixTranslate = opMatrix.glTranslatef(0,0,-0.1)
                glMultMatrixf(matrixTranslate)
            
            if keypress[pygame.K_d]:
                matrixTranslate = opMatrix.glTranslatef(-0.1,0,0)
                glMultMatrixf(matrixTranslate)
            
            if keypress[pygame.K_a]:
                matrixTranslate = opMatrix.glTranslatef(0.1,0,0)
                glMultMatrixf(matrixTranslate)
            
            if keypress[pygame.K_b]:
                matrixTranslate = opMatrix.glTranslatef(0,0.1,0)
                glMultMatrixf(matrixTranslate)
            
            if keypress[pygame.K_n]:
                matrixTranslate = opMatrix.glTranslatef(0,-0.1,0)
                glMultMatrixf(matrixTranslate)
            
            #projecao perspectiva com frustum
            if keypress[pygame.K_f]:
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()

                frustum = opMatrix.glFrustum(-1, 1, 0, 1, 1, 10) 
                glMultMatrixf(frustum)
                glMatrixMode(GL_MODELVIEW)
            
            #projecao perspectiva normal (openGl)
            if keypress[pygame.K_p]:
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                #aqui nao precisamos chamar o glMultMatrixf pois dentro das sub-rotinas do gluPerpesctive ele é chamado
                gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
                glMatrixMode(GL_MODELVIEW)
            
            #projecao ortogonal
            if keypress[pygame.K_o]:
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                d = 2
                f = (display[0]/display[1])
                ortho = opMatrix.glOrtho(-d, d, -d * f, d * f, 0.1, 50.0)
                glMultMatrixf(ortho)
                glMatrixMode(GL_MODELVIEW)
               
                
            # Apply the left and right rotation
            glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

            # Multiply the current matrix by the new view matrix and store the final view matrix 
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
            # Apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)
            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            # Light direction
            lg.direction()

            glPushMatrix()
            #glScalef(0.15, 0.15, 0.15)
            matrixScaled = opMatrix.glScaled(0.15, 0.15, 0.15)
            glMultMatrixf(matrixScaled)

            DrawFloor()
        
            glutInit(sys.argv)
            glRotate(-100, -100, 15, 15)
            
            DrawMorrinho()
            
            glTranslated(20, 40, -80)
            glRotate(-90, 10, 0, 0)

            matrixScaled = opMatrix.glScaled(5, 5, 5)
            glMultMatrixf(matrixScaled)
            DrawFURGLogo()

            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)

    pygame.quit()

if __name__ == '__main__':
    main()