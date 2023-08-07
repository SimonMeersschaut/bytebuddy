from .engine import Engine


engine = Engine()

# initialize user actions #
from .bot import bot

for attribute_name in bot.user_actions:
  # define the class-function as a function in this scope
  # (used so the user doesn't have to write bytebuddy.bot.move_forward() but rather just bytebuddy.move_forward())
  exec(f'{attribute_name} = bot.{attribute_name}')

# start world
from .world import world

# start the engine and run the game #
engine.start(bot, world)

# wait a few seconds for the engine to start
import time
time.sleep(1)


# now the main script will execute