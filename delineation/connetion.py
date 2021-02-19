import xarray as xr
import rioxarray
from .base import config
from typing import Tuple

class Connection:

    def __init__(self, config: 'Config') -> None:
        """
        :param config: config object with location attribute. Location dictionary with mapped algorithm names and
        their class names
        """
        if hasattr(config, 'location'):
            self._config = config
        else:
            raise AttributeError('Config object has no attribute "location"')

    @property
    def location(self):
        return self._config.location

    def get_data(self, dataset: str, bbox: Tuple[float, float, float, float]) -> xr.DataArray:
        pass