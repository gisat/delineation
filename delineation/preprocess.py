import xarray as xr
import rioxarray

class Preprocess:

    SPECIFICATION = {}

    def validate(self, data: xr.DataArray) -> bool:
        pass

    def resample(self, data: xr.DataArray) -> xr.DataArray:
        pass

    def reproject(self, data: xr.DataArray) -> xr.DataArray:
        pass

    def to_numpy(self, data: xr.DataArray) -> 'np.ndarray':
        pass

    def to_xarray(self, data: 'np.ndarray') -> xr.DataArray:
        pass


