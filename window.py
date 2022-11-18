from OpenGL.GL import *
import glfw

class Window:
  def resize(self, window, width, height):
    glViewport(0, 0, width, height)

  def __init__(self, width:int, height:int, title:str, drawSetup = None):    
    if not glfw.init():
      raise Exception("Wasn't possible execute the GLFW lib")

    self._win = glfw.create_window(width, height, title, None, None)
    
    if not self._win:
      glfw.terminate()
      raise Exception("Wans't possible create screen GLFW")

    glfw.set_window_pos(self._win, 400, 200)
    glfw.set_window_size_callback(self._win, self.resize)
    glfw.make_context_current(self._win)

    if drawSetup != None:
      drawSetup()

  def mainLoop(self, drawFunction = None):
    while not glfw.window_should_close(self._win):
      glfw.poll_events()
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glShadeModel(GL_SMOOTH)

      if drawFunction != None:
        drawFunction()
        
      glfw.swap_buffers(self._win)
    
  glfw.terminate()