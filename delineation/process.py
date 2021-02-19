from typing import Tuple
import xarray as xr
import rioxarray


class Process:

    def __init__(self, connection: 'Connection', preprocess: 'Preprocess', strategy: 'Strategy') -> None:
        self.connection = connection
        self.preprocess = preprocess
        self.strategy = strategy

    def process(self, algorithm:str, dataset: str, bbox: Tuple[float, float, float, float], pars: dict) -> xr.DataArray:
        xarray = self.connection.get_data(dataset, bbox)
        if self.preprocess.validate(xarray):
            input_data = self.preprocess.to_numpy(xarray)
            result = self.strategy.execute_algorithm(algorithm, input_data, pars)
            return self.preprocess.to_xarray(result)
        else:
            raise NotImplemented('Preprocessing logic is under development')

