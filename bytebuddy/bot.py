import math
import time

user_actions = []
class Bot:
  def __init__(self):
    self.x, self.y = (0, 0)
    self.direction = (1, 0)
    self.tasks_done = []
    # self.
  
  def user_action(func):
    def inner_decorator(*args, **kwargs):
      # add the action to the update-handler
      output = func(*args, **kwargs)

      # after task is complete
      self = args[0]
      self.tasks_done.append(func)

      time.sleep(.5)
      # return the output from the main action
      return output
    
    # add the function to the user_actions-list
    user_actions.append(func.__name__)

    return inner_decorator
  
  # return all user-accessible actions
  @property
  def user_actions(self):
    return user_actions
  
  def render(self, engine):
    engine.render_circle((0, 0, 255), (self.x, self.y), 10)

    # render status
    for i, finished_task in enumerate(self.tasks_done):
      engine.render_text(finished_task.__name__, (100, 20+20*i), (120, 120, 120))

  
  def update(self):
    pass

  #######################
  # define user actions # 
  #######################

  @user_action
  def move_forward(self):
    for _ in range(1000):
      self.x += self.direction[0]*0.05
      self.y += self.direction[1]*0.05
    return
  
  @user_action
  def turn_right(self):
    SPEED = 5000
    if self.direction[0] == 1:
      self.direction = (0, 1)
    elif self.direction[1] == 1:
      self.direction = (-1, 0)
    elif self.direction[0] == -1:
      self.direction = (0, -1)
    elif self.direction[1] == 1:
      self.direction = (1, 0)
    return
  
  
  

bot = Bot()