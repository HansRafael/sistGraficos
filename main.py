import pygame
from pygame.locals import *
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from draw_morrinho import DrawMorrinho
from draw_symbol import DrawSymbol
from draw_floor import DrawFloor
import sys
import lights as lg

def main():
    pygame.init()
    display = (1200, 700)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # enable aparecer na frente
    glEnable(GL_DEPTH_TEST)

    #ligths
    lg.lights()
    
    # projection and perpective
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    # init mouse movement and center mouse on screen
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
            # get keys
            keypress = pygame.key.get_pressed()
            #mouseMove = pygame.mouse.get_rel()
        
            # init model view matrix
            glLoadIdentity()

            # apply the look up and down
            up_down_angle += mouseMove[1]*0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            # init the view matrix
            glPushMatrix()
            glLoadIdentity()
            
            # apply the movment 
            if keypress[pygame.K_w]:
                glTranslatef(0,0,0.1)
            if keypress[pygame.K_s]:
                glTranslatef(0,0,-0.1)
            if keypress[pygame.K_d]:
                glTranslatef(-0.1,0,0)
            if keypress[pygame.K_a]:
                glTranslatef(0.1,0,0)
            if keypress[pygame.K_b]:
                glTranslatef(0,0.1,0)
            if keypress[pygame.K_n]:
                glTranslatef(0,-0.1,0)

            # apply the left and right rotation
            glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

            # multiply the current matrix by the get the new view matrix and store the final vie matrix 
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

            # apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)
            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            # light direction
            lg.direction()

            glPushMatrix()
            glScalef(0.15, 0.15, 0.15)

            DrawFloor()
        
            glutInit(sys.argv)
            glRotate(-100, -100, 15, 15)
            
            DrawMorrinho()
            
            glTranslated(20, 40, -80)
            glRotate(-90, 10, 0, 0)
            glScaled(5, 5, 5)
           
            DrawSymbol()

            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)

    pygame.quit()

if __name__ == '__main__':
    main()