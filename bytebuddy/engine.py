import pygame
import threading
import time
pygame.init()

class Engine:
  def __init__(self):
    self.screen = pygame.display.set_mode([500, 500])
  
  def start(self):
    t1 = threading.Thread(target=self.render_deamon)
    t1.start()
  
  def render_deamon(self):
    while True:
      self.render_frame()
      time.sleep(.5)
  
  def render_frame(self):
    self.screen.fill((255, 255, 255))
    pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()