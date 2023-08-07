import pygame
import threading
import time

class Engine:
  def start(self, bot):
    self.bot = bot
    self.t1 = threading.Thread(target=self.render_deamon)
    self.t1.start()
    time.sleep(1)
  
  def render_deamon(self):
    pygame.init()
    self.screen = pygame.display.set_mode([500, 500])
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
      self.render_frame()
    time.sleep(0.5)
  
  def render_frame(self):
    self.screen.fill((255, 255, 255))
    self.bot.update()
    self.bot.render(self)
    pygame.display.flip()
  
  def render_circle(self, color, position, radius):
    pygame.draw.circle(self.screen, color, position, radius)