"""
locator_opensky - Returning the result by the API OpenSky,
                  but with filtering the reach of the radius.
"""

from locator_opensky.public import *


try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
