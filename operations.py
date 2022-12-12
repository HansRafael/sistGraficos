from math import cos, radians, sin
import numpy as np

def glTranslatef(matrix, x,y,z):
  matrix[3][0] = matrix[3][0] + x
  matrix[3][1] = matrix[3][1] + y
  matrix[3][2] = matrix[3][2] + z
  return matrix


def glsRotateX(angle):
  matrix = [[ 1,  0,  0,  0],
      [ 0,  cos(angle), -sin(angle),  0],
      [ 0,  sin(angle),  cos(angle),  0],
      [ 0,  0, 0,  1]]
  return matrix

def glsRotateY(angle):
  matrix = [[ cos(angle),  0,  sin(angle),  0],
      [ 0,  1, 0,  0],
      [ -sin(angle),  0,  cos(angle),  0],
      [ 0,  0, 0,  1]]
  return matrix

def glsRotateZ(angle):
  matrix = [[ cos(angle),  -sin(angle),  0,  0],
      [ sin(angle),  cos(angle), 0,  0],
      [ 0, 0,  1,  0],
      [ 0,  0, 0,  1]]
  return matrix


def glScaled(x,y,z):
  matrix = [[ x,  0,  0,  0],
      [ 0,  y, 0,  0],
      [ 0,  0,  z,  0],
      [ 0,  0, 0,  1]]
  return matrix
