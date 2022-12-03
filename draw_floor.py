from OpenGL.GL import *
import OpenGL.GLUT as glut

class DrawFloor:
  def __init__(self):
    self.draw()

  def draw(self):
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-100, -100, -2)
    glVertex3f(100, -100, -2)
    glVertex3f(100, 100, -2)
    glVertex3f(-100, 100, -2)
    glEnd()