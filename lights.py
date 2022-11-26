import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def lights():
  direction = [0.0, 45.0, -1.0, 1.0]
  intensity = [1.0, 1.0, 1.0, 1]
  ambient = [0.5, 0.5, 0.5, 1]

  glEnable(GL_LIGHTING)

  glShadeModel(GL_SMOOTH)

  #enable light
  glEnable(GL_LIGHT0)
  glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
  # Define light direction and intensity
  glLightfv(GL_LIGHT0, GL_POSITION, direction)
  glLightfv(GL_LIGHT0, GL_SPECULAR, intensity)
  glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)

  #material
  glEnable(GL_COLOR_MATERIAL)
  glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
  glMaterialf(GL_FRONT, GL_SHININESS, 5.0)
  glMaterialfv(GL_FRONT, GL_SPECULAR, [0, 0, 0, 1.0])
  glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.1, 0.1, 0.1, 1.0])

def direction():
  # change postion ligh
  direction = [1, -1, 1, 0]
  glLightfv(GL_LIGHT0, GL_POSITION, direction)