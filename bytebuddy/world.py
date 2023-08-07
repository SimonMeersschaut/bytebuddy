class World:
  TILE_SIZE = 10
  def render(self, engine):
    for x in range(50):
      for y in range(50):
        engine.render_square(x*World.TILE_SIZE, y*World.TILE_SIZE, World.TILE_SIZE, World.TILE_SIZE, (50, 0, 0))



world = World()