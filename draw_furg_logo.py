from OpenGL.GL import *
import OpenGL.GLUT as glut


class DrawFURGLogo:   
    def __init__(self):
        self.draw_yellow_sphere()
        self.draw_rectangle_right()
        self.draw_rectangle_left()
        self.draw_orange_sphere()
        self.draw_red_sphere()
        self.draw_rectangle_down()
        self.draw_rectangle_down2()
        self.draw_rectangle_right2()
        self.draw_rectangle_left2()
        self.draw_yellow_rectangle_fill()
        self.draw_rectangle_fill()

    def draw_rectangle_right(self):
        glPushMatrix()
        glColor3ub(0, 0, 0) 
        glTranslated(2.5, 0, 0)
        glScaled(0.21, 2.0, -5.5)
        glut.glutSolidCube(1)
        glPopMatrix()

    def draw_rectangle_left(self):
        glPushMatrix()
        glColor3ub(0, 0, 0)
        glTranslated(-2.5, 0, 0)
        glScaled(0.21, 2.0, -5.5)
        glut.glutSolidCube(1)
        glPopMatrix()

    def draw_rectangle_right2(self):
        glPushMatrix()
        glColor3ub(0, 0, 0) 
        glTranslated(1.5, 0, 1)
        glScaled(0.21, 2.0, -5)
        glut.glutSolidCube(1)
        glPopMatrix()

    def draw_rectangle_left2(self):
        glPushMatrix()
        glColor3ub(0, 0, 0)
        glTranslated(-1.5, 0, 1)
        glScaled(0.21, 2.0, -5)
        glut.glutSolidCube(1)
        glPopMatrix()

    def draw_rectangle_down(self):
        glPushMatrix()
        glColor3ub(0, 0, 0)
        glTranslated(0, 0, -2.4)
        glScaled(5.5, 2, 0.4)
        glut.glutSolidCube(1)
        glPopMatrix()

    def draw_rectangle_down2(self):
        glPushMatrix()
        glColor3ub(0, 0, 0) 
        glTranslated(0, 0, -1.4)
        glScaled(3, 2, 0.21)
        glut.glutSolidCube(1)
        glPopMatrix()

    def draw_rectangle_fill(self):
        glPushMatrix()
        glColor3ub(255, 0, 0)
        glTranslated(0, -0.1, -1.9)
        glScaled(4.79, 2, 1)
        glut.glutSolidCube(1)
        glPopMatrix()
        

    def draw_yellow_rectangle_fill(self):
        glPushMatrix()
        glColor3ub(240, 159, 1)
        glTranslated(0, -1, 0.15)
        glScaled(2.78, 1, 2.79)
        glut.glutSolidCube(1)
        glPopMatrix()
        
    def draw_yellow_sphere(self):
        glPushMatrix()
        glColor3ub(240, 159, 1)
        glTranslated(0, 0, 1.2)
        glScaled(1.75, 1, 1.75)
        glut.glutSolidSphere(1.15, 200, 200)
        glPopMatrix()

    def draw_red_sphere(self):
        glPushMatrix()
        glColor3ub(255,0,0) 
        glTranslated(0, 0, 0.42)
        glScaled(2.45, 1, 2.45)
        glut.glutSolidSphere(1.1, 200, 200)
        glPopMatrix()

    def draw_orange_sphere(self):
        glPushMatrix()
        glColor3ub(216, 117, 14) 
        glTranslated(0, 1.6, -0.5)
        glScaled(3, 1, 3)
        glut.glutSolidSphere(1.1, 200, 200)
        glPopMatrix()


    def draw_space_left(self):
        glColor3ub(0, 0, 0)
        glTranslated(-0.39, 2.5, 0)
        glScaled(0.14, 6.15, 1)
        glut.glutSolidCube(1)

    def draw_space_right(self):
        glColor3ub(0, 0, 0)
        glTranslated(5.5, 0.1, 0)
        glScaled(1, 0.8, 1)
        glut.glutSolidCube(1)

    def draw_space_down(self):
        glColor3ub(0, 0, 0)
        glTranslated(-1.9, -0.55, 0)
        glScaled(8, 0.12, 1)
        glut.glutSolidCube(1)

    def draw_space_outside_down(self):
        glColor3ub(0, 0, 0)
        glTranslated(0, -0.82, 0)
        glScaled(5, 0.2, 1)
        glut.glutSolidCube(1)

    def draw_space_outside_left(self):
        glColor3ub(0, 0, 0)
        glTranslated(-0.155, 4, 0)
        glScaled(0.04, 10, 1)
        glut.glutSolidCube(1)

    def draw_space_outside_right(self):
        glColor3ub(0, 0, 0)
        glTranslated(7.8, 0, 0)
        glut.glutSolidCube(1)

    def draw_red_rectangle_down(self):
        glColor3ub(255, 35, 35)
        glTranslated(-3.92, -0.25, 0)
        glScaled(6.82, 0.2, 1)
        glut.glutSolidCube(1)

    def draw_space_to_border_left(self):
        glColor3ub(0, 0, 0)
        glTranslated(-0.53, 3.85, 0)
        glRotatef(-30, 0, 0, 1)
        glScaled(0.3, 0.8, 1)
        glut.glutSolidCube(1)
        glRotatef(30, 0, 0, 1)

    def draw_space_to_border_right(self):
        glColor3ub(0, 0, 0)
        glTranslated(2.9, -0.63, 0)
        glRotatef(45, 0, 0, 1)
        glScaled(0.8, 1.9, 1)
        glut.glutSolidCube(1)
        glRotatef(-38, 0, 0, 1)

    def draw_border_right(self):
        glColor3ub(255, 35, 35)
        glTranslated(-0.37, -0.5, 0)
        glScaled(0.45, 0.9, 1)
        glut.glutSolidCube(1)

    def draw_border_left(self):
        glColor3ub(255, 35, 35)
        glTranslated(-3.85, 0, 0)
        glScaled(1, 1, 1)
        glut.glutSolidCube(1)
