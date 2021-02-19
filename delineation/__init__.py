from .base import config
from .strategy import Strategy
from .preprocess import Preprocess
from .connetion import Connection
from .process import Process

__verison__ = "0.1"

_connetion = Connection(config)
_preprocess = Preprocess()
_strategy = Strategy()

process = Process(_connetion, _preprocess, _strategy)


