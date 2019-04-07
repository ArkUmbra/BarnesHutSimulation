from drawable import Drawable


class Particle(Drawable):

    def __init__(self, x, y):
        self.particleColour = (0, 0, 0)
        self.x = x
        self.y = y
        self.mass = 1

    def draw(self, d):
        # d.point((self.x, self.y), 'black')
        d.rectangle(
            [(self.x, self.y), (self.x+2, self.y+2)], 'black'
        )

    def pydraw(self, pd, surface)
        pd.rect(surface, self.particleColour, (self.x, self.y, 7, 7), 0)

    def __repr__(self):
        return '<Particle x: {}, y:{}>'.format(self.x, self.y)
