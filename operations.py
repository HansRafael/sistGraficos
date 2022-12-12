from math import cos, radians, sin
import numpy as np

def glTranslatef(x,y,z):
  matrix = [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1]]
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

def glOrtho(left, right, bottom, top, near, far):
    matrix = [[
        [2/(right-left), 0, 0, -(right+left)/(right-left)],
        [0, 2/(top-bottom), 0, -(top+bottom)/(top-bottom)],
        [0, 0, -2/(far-near), -(far+near)/(far-near)],
        [0, 0, 0, 1]
    ]]
    return matrix

def glFrustum(left, right, bottom, top, near, far):
  matrix = [[
      [2*near/(right-left), 0, (right+left)/(right-left), 0],
      [0, 2*near/(top-bottom), (top+bottom)/(top-bottom), 0],
      [0, 0, -(far+near)/(far-near), -2*far*near/(far-near)],
      [0, 0, -1, 0]
  ]]
  return matrix