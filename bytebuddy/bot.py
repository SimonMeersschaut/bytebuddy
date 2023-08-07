user_actions = []
class Bot:
  def __init__(self):
    self.x, self.y = (0, 0)
    self.update_functions_generators = []
    self.tasks_done = []
    # self.
  
  def user_action(func):
    def inner_decorator(*args, **kwargs):
      # add the action to the update-handler
      self = args[0]
      output = self.update_functions_generators.append(func(*args, **kwargs))
      print([func.__name__ for func in self.update_functions_generators])
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
    engine.render_circle((0, 0, 255), (self.x, self.y), 75)
  
  def update(self):
    # for update_function_generator in self.update_functions_generators:
    try:
      try:
        self.update_functions_generators[0].__next__()
      except IndexError:
        pass
    except StopIteration:
      self.tasks_done.append(self.update_functions_generators[0])
      self.update_functions_generators.remove(self.update_functions_generators[0])
    
  
  # define user actions # 

  @user_action
  def move_forward(self):
    '''vooruit'''
    for _ in range(10000):
      self.x += .02
      yield
    return
  
  

bot = Bot()