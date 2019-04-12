import abc


class Drawable(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pydraw(self, pd, surface):
        raise NotImplementedError('must implement pydraw function')
