from pkg_resources import get_distribution, DistributionNotFound
from .nindo import Api

api = Api()

try:
    __version__ = get_distribution('pynindo').version
except:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound
