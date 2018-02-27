"""
locator_opensky - Returning the result by the API OpenSky,
                  but with filtering the reach of the radius.
"""

from locator_opensky._public import *

__author__ = 'Ulyantsev Aleksandr (it.bumerang@gmail.com)'
__license__ = 'MIT'
__version__ = '1.0'

__all__ = ["get_nearest_ships"]


try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
