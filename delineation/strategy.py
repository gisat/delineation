from abc import ABC, abstractmethod
import numpy as np



class Strategy:
    """
    Implementation of strategy pattern for the selection of a particular algorithm  base  algorithm short name
    """

    def __init__(self, config: 'Config') -> None:
        """
        :param config: config object with strategy attribute. Strategy dictionary with mapped algorithm names and
        their class names
        """
        if hasattr(config, 'strategy'):
            self._config = config
        else:
            raise AttributeError('Config object has no attribute "strategy"')

    @property
    def algorithm(self):
        return self._config.algorithm

    def execute_algorithm(self, algorithm: str, data: np.ndarray, pars: dict) -> np.ndarray:
        """
        Return resulting ndarray from algorithm selected on the algorithm short name
        :param algorithm:
        :param data:
        :param pars:
        :return:
        """
        algorithm = self.algorithm.get(algorithm)()
        return algorithm.process(data, pars)


class Algorithm(ABC):
    """
    Algorithm interface declares operations common to all supported versions
    of some algorithm.
    """

    @abstractmethod
    def process(self, data: np.ndarray, pars: dict) -> np.ndarray:
        """
        Main method to execute delineation algorithm
        :param data: numpy array,
        :param pars: dict, parameters of clasification
        :return: numpy array,
        """
        pass


# predpis pro třídu Algorithm
class GHSLAlgorithm(Strategy):
    def process(self, data: np.ndarray, pars: dict) -> np.ndarray:
        """
        Main method to execute delineation algorithm
        :param data: numpy array,
        :param pars: dict, parameters of clasification
        :return: numpy array,
        """
        pass

