from drawable import Drawable


class Node(Drawable):


    def __init__(self, size, x, y):
        self.borderColour = (200, 200, 200)
        self.width = size[0]
        self.height = size[1]
        self.x = x
        self.y = y
        self.nodes = {"ne": None, "se": None, "sw": None, "nw": None}
        self.particle = None

    def addParticle(self, newParticle):
        if (self.isEmptyExternalNode()):
            self.particle = newParticle
            return

        if (self.nodes['ne'] is None):
            self.populateNodes()

        self.addParticleToChildNodes(self.particle)
        self.addParticleToChildNodes(newParticle)
        self.particle = None

    def populateNodes(self):
        subW = self.width / 2
        subH = self.height / 2
        subSize = (subW, subH)
        x = self.x
        y = self.y
        self.nodes["nw"] = Node(subSize, x, y)
        self.nodes["ne"] = Node(subSize, x + subW, y)
        self.nodes["se"] = Node(subSize, x + subW, y + subH)
        self.nodes["sw"] = Node(subSize, x, y + subH)

    def addParticleToChildNodes(self, particle):
        if (particle is None):
            return

        for node in self.nodes.values():
            if (node.boundsAround(particle)):
                node.addParticle(particle)
                return

        # Node has fallen out of bounds, so we just eat it
        # raise Exception('particle added to wrong node')
        print ('Node moved out of bounds')

    def boundsAround(self, particle):
        return (particle.x >= self.x
                and particle.y >= self.y
                and particle.x < self.x + self.width
                and particle.y < self.y + self.height)

    def draw(self, d):
        d.rectangle(
            [(self.x, self.y),
            (self.x + self.width, self.y + self.height)],
            fill=None,
            outline='grey')

        if (self.particle is None):
            for node in self.nodes.values():
                if (node is not None):
                    node.draw(d)
        else:
            self.particle.draw(d)

    def pydraw(self, pd, surface):
        pd.rect(surface, self.borderColour,
            (self.x, self.y, self.width, self.height), 1)

        if (self.particle is None):
            for node in self.nodes.values():
                if (node is not None):
                    node.pydraw(pd, surface)
        else:
            self.particle.pydraw(pd, surface)

    def isExternalNode(self):
        return self.nodes['ne'] is None

    def isEmptyExternalNode(self):
        return self.isExternalNode() and self.particle is None

    def __repr__(self):
        return '<Node x: {}, y:{}, width:{}, height:{}, particle:{}, nodes:{}>'.format(self.x, self.y, self.width, self.height, self.particle, self.nodes)
