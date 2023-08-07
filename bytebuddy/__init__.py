from .engine import Engine

# add all actions such as move_forward() #
# this import is wildcard on purpose so the user can access the actions directly from their script #
from .bot.bot import * 

engine = Engine()
engine.start()