import pygame
import threading
import time

class Engine:
  def start(self, bot, world):
    self.bot = bot
    self.world = world
    self.t1 = threading.Thread(target=self.render_deamon)
    self.t1.start()
    self.font = pygame.font.SysFont('chalkduster.ttf', 40)
  
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
    # self.screen.fill((0, 0, 0))
    self.world.render(self)
    self.bot.update()
    self.bot.render(self)
    pygame.display.flip()
  
  def render_circle(self, color, position, radius):
    pygame.draw.circle(self.screen, color, position, radius)
  
  def render_square(self, x, y, width, height, color):
    pygame.draw.rect(self.screen, color, pygame.Rect(x, y, width, height))
  
  def render_text(self, text, position, color):
    img = self.font.render(text, True, color)
    self.screen.blit(img, position)