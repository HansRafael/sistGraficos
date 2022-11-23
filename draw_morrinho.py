from OpenGL.GL import *
import random
import OpenGL.GLUT as glut
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy
from draw_symbol import DrawSymbol

from window import Window



class DrawMorrinho:
    def __init__(self):
        self.tree = Image.open('tree_texture.jpg').convert('RGBA')
        self.height = self.tree.height
        self.width = self.tree.width
        self.image_content = numpy.array(list(self.tree.getdata()), numpy.uint8)
        self.scale = 2.0
        self.rotate_y = 0.0
        self.rotate_x = 0.0
        self.draw_floor()
        
        
    def special(self, key, x):
        # Rotate cube according to keys pressed
        angle = random.choice([0, 20, 30, 50, 60])
        if key == GLUT_KEY_RIGHT:
            glRotate(angle, 0, 1, 0)
        if key == GLUT_KEY_LEFT:
            glRotate(angle, 0, 1, 0)
        if key == GLUT_KEY_UP:
            glRotate(angle, 0, 1, 0)
        if key == GLUT_KEY_DOWN:
            glRotate(angle, 0, 1, 0)
        glutPostRedisplay()

    def draw_floor(self):
        glScaled(7, 5, 7)
        glTranslated(0, 0.5, 0)
        glColor3f(0.0, 1, 0.0)
        glTranslated(1, -1.3, 0)
        glScaled(1.1, 1, 1)
        glut.glutSolidSphere(-1, 20, 20)
        self.draw_tree()
        glTranslated(3, -50, -2)
        glScaled(8, 50, 8)
        self.draw_tree()
        glTranslated(-7, -70, 2)
        glScaled(8, 50, 8)
        self.draw_tree()
        glTranslated(-4, -70, 2)
        glScaled(8, 50, 8)
        self.draw_tree()
        glTranslated(15, -70, 0)
        glScaled(8, 50, 8)
        self.draw_tree()
        glTranslated(4, -70, -2)
        glScaled(8, 50, 8)
        self.draw_tree()
        glTranslated(-10, -10, -1)
        glScaled(8, 50, 8)
        self.draw_tree()
        glTranslated(-7, -80, 15)
        glScaled(8, 50, 8)
        glColor3f(0.0, 1, 0.0)
        glut.glutSolidSphere(-1, 20, 20)
        self.draw_tree()
        glTranslated(-7, -80, 5)
        glScaled(8, 55, 8)
        glColor3f(0.0, 1, 0.0)
        glut.glutSolidSphere(-1, 20, 20)
        self.draw_tree()

    def draw_tree(self):
        self.enable_tree_texture()
        glColor3ub(150, 75, 0)
        glScaled(0.05, 2, 0.05)
        glut.glutSolidSphere(1, 200, 200)
        self.disable_texture()
        glTranslated(0, 1, 0)
        glScaled(1, 0.01, 1)
        glColor3ub(0, 128, 0)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.2, 1, 1.2)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.5, 1, 1.5)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.8, 1, 1.8)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(0.8, 1, 0.8)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1, 1, 1)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.5, 1, 1.5)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.2, 1, 1.2)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(0.8, 1, 0.8)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.2, 1, 1.2)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1, 1, 1)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.8, 1, 1.8)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(0.8, 1, 0.8)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(0.8, 1, 0.8)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.2, 1, 1.2)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1.5, 1, 1.5)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(1, 1, 1)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(0.8, 1, 0.8)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(0.6, 1, 0.6)
        glut.glutSolidCube(1)
        glTranslated(0, -2, 0)
        glScaled(0.5, 1, 0.5)
        glut.glutSolidCube(1)

    def enable_tree_texture(self):
        glEnable(GL_TEXTURE_2D)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE,
                     self.image_content)
        glGenerateMipmap(GL_TEXTURE_2D)

    def disable_texture(self):
        glDisable(GL_TEXTURE_2D)
