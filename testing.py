import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from draw_morrinho import DrawMorrinho
from draw_furg_logo import DrawFURGLogo
import sys,pygame

def display():
  # Clear the color and depth buffers
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  
  # Enable z-buffer
  glEnable(GL_DEPTH_TEST)
  glDepthFunc(GL_LEQUAL)
  glDisable(GL_CULL_FACE)
  glCullFace(GL_BACK)

  glEnable(GL_FOG)
  glPushMatrix()
  glScalef(0.15, 0.15, 0.15)
  angle = random.choice([0, 20, 30, 50, 60])

  time_control = 2

  if time_control < 5 or time_control > 15:
    glDisable(GL_LIGHTING)
    DrawFURGLogo()
  else:
    glRotate(0, 10, 11, 10)
    DrawMorrinho()
  glPopMatrix()
  glutSwapBuffers()
  



glutInit(sys.argv)

# Create a double-buffer RGBA window
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Create a window, setting its title
glutInitWindowSize(800, 600)
glutCreateWindow('FURG')

# Set the display callback
glutDisplayFunc(display)


# Run the GLUT main loop until the user closes the window
glutMainLoop()

