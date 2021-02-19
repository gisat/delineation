from delineation.base import config
from delineation.strategy import Strategy
from delineation.preprocess import Preprocess
from delineation.connetion import Connection
from delineation.process import Process

__verison__ = "0.1"


class Delineation:

    def __init__(self):
        self.prcess = Process(Connection(config), Preprocess(), Strategy())

    @property
    def process(self, algorithm, dataset, bbox, pars):
        return self.prcess.process(algorithm, dataset, bbox, pars)