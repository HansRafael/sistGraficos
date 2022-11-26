import pygame
from pygame.locals import *
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from draw_morrinho import DrawMorrinho
from draw_symbol import DrawSymbol
import math, sys

pygame.init()
display = (1200, 700)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

sphere = gluNewQuadric() 

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

up_down_angle = 0.0
paused = False
run = True

def lights():
  ambient_intensity = [1, 1, 1, 1.0]

  direction = [0.0, 45.0, -1.0, 1.0]

  intensity = [1, 0.7, 1, 1.0]

  # Enable light
  glEnable(GL_LIGHTING)

  # Define light model
  glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_intensity)

  # Enable light 0
  glEnable(GL_LIGHT0)

  # Define light direction and intensity
  glLightfv(GL_LIGHT0, GL_POSITION, direction)
  glLightfv(GL_LIGHT0, GL_SPECULAR, intensity)
  glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)

  # Config material
  glEnable(GL_COLOR_MATERIAL)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  glMaterialf(GL_FRONT, GL_SHININESS, 5.0)
  glMaterialfv(GL_FRONT, GL_SPECULAR, [0, 0, 0, 1.0])
  glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.1, 0.1, 0.1, 1.0])


def enable_tree_texture(self):
    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE,
                  self.image_content)
    glGenerateMipmap(GL_TEXTURE_2D)

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

        # change postion
        direction = [1, -1, 1, 0]
        glLightfv(GL_LIGHT0, GL_POSITION, direction)
        

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glScalef(0.15, 0.15, 0.15)
        glColor4f(1.0, 0.5, 0.0, 0.0)
        
        glBegin(GL_QUADS)
        glVertex3f(-100, -100, -2)
        glVertex3f(100, -100, -2)
        glVertex3f(100, 100, -2)
        glVertex3f(-100, 100, -2)
        glEnd()
        
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
