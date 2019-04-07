import abc


class Drawable(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self, d):
        raise NotImplementedError('must implement draw function')

    @abc.abstractmethod
    def pydraw(self, pd, surface):
        raise NotImplementedError('must implement pydraw function')
